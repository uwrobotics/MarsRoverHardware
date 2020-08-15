# Low Power Brushed Motor Controller Board

Motor controller board for low power brushed DC motors (12V).

## Motor Driver IC
* [VNH7070AS](https://www.digikey.ca/product-detail/en/stmicroelectronics/VNH7070ASTR/497-17630-1-ND/7691023)
    * Output current: 15A
    * Maximum supply voltage: 38V 

## Motors

* [12V 131:1 Gear Motor w/Encoder](https://www.robotshop.com/en/12v-1311-gear-motor-encoder.html#Specifications)
* [Heavy Duty Rod Actuators](https://www.firgelliauto.ca/collections/400lbs-to-1000lbs/products/heavy-duty)
* [30:1 Metal Gearmotor 37Dx68L mm 12V with 64 CPR Encoder](https://www.pololu.com/product/4752)

## Reverse Polarity Protection
The reverse polarity protection circuit uses a P-channel MOSFET (or PMOS) which conducts current when the applied gate voltage is high and does not conduct when the applied gate voltage is low. In the case that the 12V and GND references are reversed, a high voltage level is experienced at the gate, causing the PMOS to switch off and act as an open circuit.

![Reverse Polarity Protection Circuit](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Low%20Power%20Brushed%20Motor%20Controller/Rev1/images/rpp_circuit.png)

## Images
![Assembled PCB](https://github.com/uwrobotics/MarsRover2020-PCB/blob/master/Projects/Low%20Power%20Brushed%20Motor%20Controller/Rev1/images/assembled_board.jpg)

## Contributors

* **Kyle Hong** - *Schematic Capture* - [Scotrus](https://github.com/Scotrus)
* **Cindy Li** - *PCB Design* - [cindyli-13](https://github.com/cindyli-13)

## Built With

* [Altium Designer](https://www.altium.com/) - PCB design software used

## Errata
* Fix P-Channel MOSFET footprint
* Fix Zener diode footprint cathode indicator