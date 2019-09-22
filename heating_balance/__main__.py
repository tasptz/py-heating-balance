import yaml
import argparse
from collections import OrderedDict

from . import *

def load_surfaces(data, g):
    surfaces = []
    for ls in data['surfaces']:
        windows = [
            Window(
                w['area'] * m2,
                w['glass_area_ratio'],
                w['u'] * u,
                w['g'],
                g(ls['solar_radiation'], W / m2))
            for w in ls['windows']] if 'windows' in ls else []
        temperature_conditioned = g(ls['temperature_conditioned'], C) \
            if 'temperature_conditioned' in ls else None
        surfaces.append(Surface(ls['area'] * m2,
                                ls['u'] * u,
                                ls['u_correction'],
                                temperature_conditioned,
                                windows))
    return surfaces

def main():
    parser = argparse.ArgumentParser(prog='heating_balance')
    parser.add_argument('building', type=str)
    args = parser.parse_args()

    with open(args.building, 'r') as f:
        d = yaml.load(f, Loader=yaml.SafeLoader)
    
    rows = OrderedDict()
    for condition_id in d['conditions'].keys():
        def g(v, unit=''):
            if isinstance(v, dict):
                v = v[condition_id]
            return with_unit(v, unit)

        internal_gain = g(d['internal_gain'], W)
        air_temperature_outside = g(d['air_temperature_outside'], C).to(K)
        air_temperature_inside = g(d['air_temperature_inside'], C).to(K)
           
        surfaces = load_surfaces(d, g)

        volume = Volume(d['volume'] * m3,
                        d['air_volume_ratio'],
                        surfaces,
                        air_temperature_inside)

        surface_loss = volume.surface_loss(air_temperature_outside)
        solar_gain = volume.solar_gain()

        ventilation = Ventilation(d['ventilation_air_change_rate'] / hour,
                                  air_temperature_outside,
                                  with_unit(d['ventilation_efficiency']))
        ventilation_loss = volume.ventilation_loss(ventilation)

        leakage = Ventilation(d['ventilation_leakage'] / hour,
                              air_temperature_outside,
                              0.0)
        leakage_loss = volume.ventilation_loss(leakage)

        def append(k, v, s='{:+8.2f}'):
            rows.setdefault(k, []).append((v, s))
        append('Living space', d['living_space'] * m2)
        append('Air inside', air_temperature_inside.to(C))
        append('Air outside', air_temperature_outside.to(C))
        append('Air volume', volume.air())
        append('Surface', sum(s.area for s in surfaces))
        append('Surface loss', -surface_loss)
        append('Ventilation', ventilation.change_rate)
        append('Ventilation eff.', ventilation.efficiency, '{:8.1%}')
        append('Ventilation loss', -ventilation_loss)
        append('Leakage', leakage.change_rate)
        append('Leakage loss', -leakage_loss)
        append('Windows', sum(w.area for s in surfaces for w in s.windows))
        append('Solar gain', solar_gain)
        append('Internal gain', internal_gain)
        heat_balance = solar_gain + internal_gain - (surface_loss + ventilation_loss + leakage_loss)
        append('Heat balance', heat_balance)
        append('Heat balance / m2', heat_balance / (d['living_space'] * m2))

    pt = PrettyTable([''] + list(d['conditions'].values()))
    with open(os.path.splitext(sys.argv[1])[0] + '.csv', 'w') as csvfile:
        w = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ['']
        for v in d['conditions'].values():
            header += [v, '']
        w.writerow(header)
        for k, v in rows.items():
            w.writerow([k] + sum([[x[0].magnitude, str(x[0].units)] for x in v], []))  # sum flattens nested lists
            pt.add_row([k] + [x[1].format(x[0]) for x in v])
    pt.align = 'l'
    print(pt)

if __name__ == '__main__':
    main()
