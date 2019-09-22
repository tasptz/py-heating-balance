# Heating Balance
A very simple python module to gauge the energy needed to keep a building heated.
The module considers
 * surface loss
 * ventilation and leakage loss
 * solar gain
 * internal gain
 * physically correct units

## Example
`example.yaml` contains a commented example of a tiny house.
Calling

```python -m heating_balance example.yaml```

prints the following results, which are also exported to a csv file.
```
+-------------------+-------------------------+--------------------------+--------------------------+
|                   | very cold but sunny     | very cold & overcast     | cold & overcast          |
+-------------------+-------------------------+--------------------------+--------------------------+
| Living space      | +25.00 meter ** 2       | +25.00 meter ** 2        | +25.00 meter ** 2        |
| Air inside        | +20.00 degC             | +20.00 degC              | +20.00 degC              |
| Air outside       | -15.00 degC             | -10.00 degC              | -5.00 degC               |
| Air volume        | +37.50 meter ** 3       | +37.50 meter ** 3        | +37.50 meter ** 3        |
| Surface           | +125.00 meter ** 2      | +125.00 meter ** 2       | +125.00 meter ** 2       |
| Surface loss      | -526.75 watt            | -451.50 watt             | -376.25 watt             |
| Ventilation       | +0.40 / hour            | +0.40 / hour             | +0.40 / hour             |
| Ventilation eff.  | 83.0%                   | 83.0%                    | 83.0%                    |
| Ventilation loss  | -30.00 watt             | -25.72 watt              | -21.43 watt              |
| Leakage           | +0.04 / hour            | +0.04 / hour             | +0.04 / hour             |
| Leakage loss      | -18.53 watt             | -15.88 watt              | -13.24 watt              |
| Windows           | +4.50 meter ** 2        | +4.50 meter ** 2         | +4.50 meter ** 2         |
| Solar gain        | +320.00 watt            | +16.00 watt              | +16.00 watt              |
| Internal gain     | +125.00 watt            | +125.00 watt             | +125.00 watt             |
| Heat balance      | -130.28 watt            | -352.10 watt             | -269.91 watt             |
| Heat balance / m2 | -5.21 watt / meter ** 2 | -14.08 watt / meter ** 2 | -10.80 watt / meter ** 2 |
+-------------------+-------------------------+--------------------------+--------------------------+
```
## Installation
`pip install -r requirements.txt` shoud be sufficient.

## Data
To calculate surface properties [u-wert-rechner](https://www.ubakus.de/u-wert-rechner/?&lang=en) can be used.
Window and ventilation characteristics should be obtainable from the respective supplier.