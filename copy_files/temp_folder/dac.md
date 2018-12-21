# Unit DAC

<img src="assets/img/product_pics/units/M5GO_Unit_dac.png" width="30%" height="30%"><img src="assets/img/product_pics/units/unit_dac_grove_a.png" width="30%" height="30%">

***

:memo:**[Description](#Description)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:octocat:**[Example](#Example)**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :electric_plug:**[Schematic](#Schematic)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🛒**[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-Mini-DAC-Unit-with-DHT12-BMP280-Digital-DHT-12-Temperature-Humidity-Aire-Pressure-Sensor/3226069_32933115893.html?spm=2114.12010615.8148356.2.758c5bcbURtQtR)**

## Description

This is a unit can convert digital signal to analog signal like voltage waveform, audio waveform and so on. It integrates a 12-bit high resolution DAC chip named MCP4725 which integrates a on-board non-volatile memory (EEPROM). The unit comunicates with M5Core with I2C. The DAC input and configuration data can be programmed to the EEPROM.

## Feature

-  Up to 12 bits of resolution
-  Output 0~3.3V voltage
-  GROVE interface, support [UiFlow](http://flow.m5stack.com) and [Arduino](http://www.arduino.cc)
-  Two Lego installation holes

## APPLICATION

-  MP3 Audio Player
-  mini Oscilloscope

## Related Link

-  **Example** - [Arduino](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/DAC_MCP4725)

-  **Datasheet** - [MCP4725](http://pdf1.alldatasheet.com/datasheet-pdf/view/233449/MICROCHIP/MCP4725.html)

-  **[Purchase](https://www.aliexpress.com/store/product/M5Stack-Official-DAC-Unit-MCP4725-I2C-DAC-Converter-Breakout-Module-Digital-to-Analog-12-Bits-0V/3226069_32947696641.html?spm=a2g1x.12024536.productList_5885013.pic_6)**

## Example

```c++
float tmp = dht12.readTemperature();//temperature
float hum = dht12.readHumidity();//humidity
float pressure = bme.readPressure();//pressure
```

Click [here](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Units/DAC)for Specific example.

## Schematic

<img src="assets/img/product_pics/units/dac_sch.JPG">

### PinMap

<table>
 <tr><td>M5Core(GROVE A)</td><td>GPIO22</td><td>GPIO21</td></tr>
 <tr><td>DAC Unit</td><td>SCL</td><td>SDA</td></tr>
</table>