# Arm Board

The arm board is responsible for the control of the rover's 6-DOF robotic arm. The MCU onboard is the [STM32F446VET7](https://www.st.com/resource/en/datasheet/stm32f446re.pdf). This PCB interfaces with force sensitive resistor, servo motor, linear actuator, three brushed DC motor drivers, three absolute encoders, three relative integrated encoders, and ten limit switches.
![alt_text](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Arm/Rev1/Arm_Render.png)

## Block Diagram

![alt text](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Arm/Rev1/ArmBlockDiagram.png)

## Peripherals

### Motor Controllers

* [Cytron MDD10A](https://www.cytron.io/p-10amp-5v-30v-dc-motor-driver-2-channels) - 10Amp 5V-30V Dual Channel DC Motor Driver
* [Cytron MD30C](https://www.cytron.io/p-30amp-5v-30v-dc-motor-driver) - 30Amp 5V-30V DC Motor Driver

### Servo

* [SG90](http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf) - Micro servo motor


### Limit Switches

* [Twidec Limit Switch](https://www.amazon.ca/gp/product/B07NVDXGPS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) - Short Hinge Roller Lever Arm Switch
* [Cylewet Limit Switch](https://www.amazon.ca/gp/product/B07DGX5Q1Q/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) - Long Straight Hinge Lever Arm Switch

### Force Sensitive Resistor

* [Interlink Electronics FSR 402](https://cdn.sparkfun.com/assets/8/a/1/2/0/2010-10-26-DataSheet-FSR402-Layout2.pdf) - 18.28mm diameter force sensitive resistor


### Encoders

* [US Digital MAE3](https://www.usdigital.com/products/encoders/absolute/magnetic/MAE3) - Absolute magnetic kit encoder with PWM output. 10/12 bit
* [Broadcom AEAT-6012-A06](https://www.broadcom.com/products/motion-control-encoders/magnetic-encoders/aeat-6012-a06) - 12-bit magnetic encoder with SPI output

## Contributors

* **Kyle Hong** - *MCU config and consolidated connectors* - [Scotrus](https://github.com/Scotrus)
* **Princely Onaifo** - *MCU config* - [Princely-O](https://github.com/Princely-O)
* **Noah Chapman** - *SPI encoder circuit* - [Nzyme](https://github.com/Nzyme)
* **Ayesha Ebrahim** - *Force sensitive resistor circuit* - [a-ebrahim](https://github.com/a-ebrahim)


## Built With

* [Altium Designer](https://www.altium.com/) - PCB design software used
