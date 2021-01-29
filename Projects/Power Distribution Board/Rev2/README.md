# Power Distribution Board

The Power Distribution Board takes as input 24V power from a 6s1p battery pack and supplies 24V power to the ethernet switch, 17V power to the Nvidia Jetson board, and 5V power to custom PCBs onboard the Mars rover robot. 

DC power conversion is carried out through a buck-boost converter for 24V and buck converters for 17V and 5V. Battery reverse polarity protection is achieved through an ideal diode controller and external N-channel MOSFET. Each load is controlled by a high-side smart switch with open-load detection and current limiting capabilities. 

The PDB also serves to control the LED Matrix board and interface with four URM04 ultrasonic sensors placed at the four corners of the rover to detect close-range obstacles.

## Block Diagram

![Block Diagram](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Power%20Distribution%20Board/Rev2/Images/PDB_Rev2_Block_Diagram.png)

## Ultrasonic Sensors

* [SEN0002 URM04 V2.0](https://wiki.dfrobot.com/URM04_V2.0__SKU_SEN0002_)

## Images

![Assembled PCB](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Power%20Distribution%20Board/Rev2/Images/PDB_Rev2_Assembled.jpg)

## Designers

* **Cindy Li** - *Schematic Capture and PCB design* - [cindyli-13](https://github.com/cindyli-13)

## Built With

* [Altium Designer](https://www.altium.com/) - The PCB design software used

## Errata

* Introduce enable signals to load switches
* Add line driver / receiver control signal to MAX485 transceiver
* Fix test point silkscreen labels
* Fix 24V buck-boost issue
