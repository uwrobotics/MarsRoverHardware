# Gimbal/Autonomy

The Gimbal/Autonomy board is resonsible for both controlling the movement of the rover's camera gimbal
and accommodating the ultrasonic sensors and LED matrix for autonomous operation.

## Block Diagram



## Peripherals


### LED Matrix

* [NeoPixel WS2812](https://cdn-shop.adafruit.com/datasheets/WS2812.pdf) - Intelligent RGB LED


### Servo Motors

* [Hitec HSR-1425CR](https://hitecrcd.com/products/servos/robotic-servos/hsr1425/product) - 5V Continuous Rotation Servo Motor
* [Hitec HS-645](https://hitecrcd.com/products/servos/sport-servos/analog-sport-servos/hs-645mg/product) - 5V Standard Servo Motor


### Encoders

* [US Digital MAE3](https://www.usdigital.com/products/encoders/absolute/magnetic/MAE3) - Absolute Encoder (PWM)
* [Broadcom AEAT-6012](https://www.broadcom.com/products/motion-control-encoders/magnetic-encoders/aeat-6012-a06) - Absolute Encoder (SPI)


## Sensors

* [JSN-SR04T V2.0](https://www.makerfabs.com/water-proof-ultrasonic-ranger-jsn-sr04t-v2.0.html) - Ultrasonic Sensors


## Images
![Assembled PCB](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Gimbal/Rev1/images/Rev1%20Assembled%20Board.jpg)


## Designers

* **Aidan Gratton** - *PCB Design* - [a-gratton](https://github.com/a-gratton)
* **Jing Hao Yao** - *Schematic Capture* - [JingHaoYao](https://github.com/JingHaoYao)
* **Caitlyn Mei** - *Routing* - [caitlynxymei](https://github.com/caitlynxymei)


## Built With

* [Altium Designer](https://www.altium.com/) - The PCB design software used
* [OSHStencils](https://www.oshstencils.com/) - The PCB stencil maker used


## Errata

* 5V level shifter bypass capacitor (C19) is not next to IC, it is currently beside the voltage regulator
* SPI1_MISO should be level shifted since MCU pins are not 5V tolerant
* Team logo and designer names should be added to silkscreen
* Need fusing for ultrasonic sensors
* Silkscreen should be made 60mils

