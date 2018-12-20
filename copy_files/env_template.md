# Unit ENV

<img src="assets/img/product_pics/units/M5GO_Unit_env.png" width="30%" height="30%"><img src="assets/img/product_pics/units/unit_env_grove_a.png" width="30%" height="30%">

***

:memo:**[Description](#Description)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:octocat:**[Example](#Example)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :electric_plug:**[Schematic](#Schematic)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🛒**[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-Mini-ENV-Unit-with-DHT12-BMP280-Digital-DHT-12-Temperature-Humidity-Aire-Pressure-Sensor/3226069_32933115893.html?spm=2114.12010615.8148356.2.758c5bcbURtQtR)**

## Example

```c++
float tmp = dht12.readTemperature();//temperature
float hum = dht12.readHumidity();//humidity
float pressure = bme.readPressure();//pressure
```

Click [here](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Units/ENV)for Specific example.

## Schematic

<img src="assets/img/product_pics/units/env_sch.JPG">

### PinMap

<table>
 <tr><td>M5Core(GROVE A)</td><td>GPIO22</td><td>GPIO21</td></tr>
 <tr><td>ENV Unit</td><td>SCL</td><td>SDA</td></tr>
</table>