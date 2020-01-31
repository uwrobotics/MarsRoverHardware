# Gimbal/Autonomy

The Gimbal/Autonomy board is resonsible for both controlling the movement of the rover's camera gimbal
and accommodating the ultrasonic sensors and LED matrix for autonomous operation.

## Block Diagram



## Peripherals


### LED Matrix

* 


### Servo Motors

* [Hitec HSR-1425CR](https://www.servocity.com/hsr-1425cr-servoSS) - 5V Continuous Rotation Servo Motor
* [Hitec HS-645](https://www.servocity.com/hs-645mg-servo) - 5V Standard Servo Motor


### Limit Switches

* TBD


### Encoders

* TBD


## Sensors

* Ultrasonic Sensors (TBD)


## Images
![Assembled PCB](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Gimbal/Rev1/Rev1%20Assembled%20Board.jpg)


## Designers

* **Aidan Gratton** - *PCB Design* - [a-gratton](https://github.com/a-gratton)
* **Jing Hao Yao** - *Schematic Capture* - [Jing Hao Yao](https://github.com/JingHaoYao)
* **Caitlyn Mei** - *Routing* - [caitlynxymei](https://github.com/caitlynxymei)


## Built With

* [Altium Designer](https://www.altium.com/) - The PCB design software used
* [OSHStencils](https://www.oshstencils.com/) - The PCB stencil maker used


## Errata

* 5V level shifter bypass capacitor (C19) is not next to IC, it is currently beside the voltage regulator
* SPI1_MISO should be level shifted
* Team logo and designer names should be added to silkscreen


