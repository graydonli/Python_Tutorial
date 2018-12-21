# Unit DUAL_BUTTON

<img src="assets/img/product_pics/units/M5GO_Unit_dual_button.png" width="30%" height="30%"><img src="assets/img/product_pics/units/unit_dual_button_grove_a.png" width="30%" height="30%">

***

:memo:**[Description](#Description)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:octocat:**[Example](#Example)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :electric_plug:**[Schematic](#Schematic)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🛒**[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-Mini-DUAL_BUTTON-Unit-with-DHT12-BMP280-Digital-DHT-12-Temperature-Humidity-Aire-Pressure-Sensor/3226069_32933115893.html?spm=2114.12010615.8148356.2.758c5bcbURtQtR)**

## Description

This Unit is a dual-button unit that can be detected whether a single button pressed or two buttons pressed

## Feature

-  GROVE interface, support [UiFlow](http://flow.m5stack.com) and [Arduino](http://www.arduino.cc)
-  Two Lego installation holes

## Related Link

<!-- - **[Example](en/file_to_display_null)** -->
- **[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-New-Mini-Dual-Button-Unit-Mini-with-GROVE-Port-Cable-Connector-Compatible-with-FIRE/3226069_32923126250.html?spm=a2g1x.12024536.productList_2187621.9)**

## Example

```c++
float tmp = dht12.readTemperature();//temperature
float hum = dht12.readHumidity();//humidity
float pressure = bme.readPressure();//pressure
```

Click [here](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Units/DUAL_BUTTON)for Specific example.

## Schematic

<img src="assets/img/product_pics/units/dual_button_sch.JPG">

### PinMap

<table>
 <tr><td>M5Core(GROVE A)</td><td>GPIO22</td><td>GPIO21</td></tr>
 <tr><td>DUAL_BUTTON Unit</td><td>SCL</td><td>SDA</td></tr>
</table>