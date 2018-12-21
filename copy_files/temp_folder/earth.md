# Unit EARTH

<img src="assets/img/product_pics/units/M5GO_Unit_earth.png" width="30%" height="30%"><img src="assets/img/product_pics/units/unit_earth_grove_a.png" width="30%" height="30%">

***

:memo:**[Description](#Description)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:octocat:**[Example](#Example)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :electric_plug:**[Schematic](#Schematic)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🛒**[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-Mini-EARTH-Unit-with-DHT12-BMP280-Digital-DHT-12-Temperature-Humidity-Aire-Pressure-Sensor/3226069_32933115893.html?spm=2114.12010615.8148356.2.758c5bcbURtQtR)**

## Description

<mark>EARTH</mark> is a moisture detective unit for measuring the moisture in soil. The soil moisture sensor is pretty straight forward to use. The two large exp osed pads function as probes for the sensor, together acting as a variable resistor. The more water that is in the soil means the better the conductivity between the pads will be and will result in a lower resistance, and a higher SIG out.
You can read the moisture in soil staright or get a digital signal(0/1) that means the high(or low) humidity.

## Feature

-  Adjustable threshold, including 10K adjustable resistor
-  Analog & Digital output
-  GROVE interface, support [UiFlow](http://flow.m5stack.com) and [Arduino](http://www.arduino.cc)
-  Two Lego installation holes

## Related Link

-  **Example** - [Arduino](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/Earth)
- **[Schematic](https://github.com/m5stack/M5-Schematic/blob/master/Units/UNIT_EARTH.pdf)**
- **[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-Earth-Module-Grove-Compatible-Soil-monitoring-Analog-and-Digital-Output/3226069_32922643696.html?spm=2114.12010615.8148356.2.45434ff2lDdyLQ)**

## Example

```c++
float tmp = dht12.readTemperature();//temperature
float hum = dht12.readHumidity();//humidity
float pressure = bme.readPressure();//pressure
```

Click [here](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Units/EARTH)for Specific example.

## Schematic

<img src="assets/img/product_pics/units/earth_sch.JPG">

### PinMap

<table>
 <tr><td>M5Core(GROVE A)</td><td>GPIO22</td><td>GPIO21</td></tr>
 <tr><td>EARTH Unit</td><td>SCL</td><td>SDA</td></tr>
</table>