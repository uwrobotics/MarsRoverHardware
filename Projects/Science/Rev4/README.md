# Science Board

The science board is responsible for interfacing with the motors, servos, and sensors in the rover's science data collection module.
The science module consists of two primary components; the digger used to collect soil samples and the centrifuge used to mix soil samples with chemicals 
The science module will test the dampness of soil sites using the STEMMA moisture sensor to determine where to retreive soil samples.
The digger has two sub-modules the scoop and the lift.
The scoop uses the Hitec HS-82MG servo to collect soil samples.
The lift raises and lowers the scoop using a Pololu 4695.
At the top of the lift the sample into the centrifuge.
The centrifuge consists of two components; the lid and the geniva drive used to rotate the centrifuge.
The lid is controlled by the Feetech FS90 servo.
The geniva drive is driven by Pololu 4685.

![Science_Render](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Science/Rev1/images/Science_Render.jpg)

## Block Diagram

![Block Diagram](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Science/Rev1/images/Science_Block_Diagram.png)

## Actuators

### Motor Controllers

* [Cytron 10A 5-30V Dual Channel DC Motor Driver](https://www.robotshop.com/ca/en/cytron-10a-5-30v-dual-channel-dc-motor-driver.html)

### Servos

* [Feetech FS90](https://www.pololu.com/product/2818) - 9g analog servo
* [Hitec HS-82MG](https://hitecrcd.com/products/servos/micro-and-mini-servos/analog-micro-and-mini-servos/hs-82mg/product) - Metal gear micro servo 

### Motors

* [Pololu 4693 motor](https://www.pololu.com/product/4693)
* [Pololu 4685 motor](https://www.pololu.com/product/4685)

## Sensors

* [Adafruit STEMMA Soil Sensor](https://www.adafruit.com/product/4026) - I2C capacitive moisture sensor

## Images

## Designers

* **Wolfgang Windholtz** - *Schematic and PCB design* - [WolfgangWindholtz](https://github.com/WolfgangWindholtz)

## Built With

* [Altium Designer](https://www.altium.com/) - The PCB design software used

## Errata

* TBD
