# University of Waterloo Mars Rover 2021 Hardware Repository
This repository contains:
- Altium libraries [[Libraries](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Libraries)]
- PCB designs [[Projects](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Projects)]
- Altium templates [[Templates](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Templates)]

Further descriptions and instructions for using each individual board are available in the README in the relevant board's directory.

## System Block Diagram
![Alt Text](https://github.com/uwrobotics/MarsRover2021-hardware/blob/master/System_block_diagram.png)

## Hardware Development Instructions

1. Download [Diptrace](https://diptrace.com/download/download-diptrace/)
2. Complete the [555 timer PCB tutorial](https://docs.google.com/document/d/1YiGjYYuB-FUKcaG-C9Ers9Dd0e59WRM9QEbI4RcCCmw/edit?usp=sharing) in Diptrace
3. Request Altium license from [Lance Bantoto](https://github.com/lwbantoto)
4. Download [Altium Designer 20.1.7](https://www.altium.com/products/downloads/)
5. Download [Saturn PCB Toolkit](http://www.saturnpcb.com/pcb_toolkit/)
6. Clone repository
    - `git clone https://github.com/uwrobotics/MarsRover2021-hardware.git`
7. Read the [wiki](https://github.com/uwrobotics/MarsRover2020-PCB/wiki)

## Best Practices and Tips
- Preface your commit message with the project name. For example "ARM: add TVS diode" or "LIBRARY: add 10K 0603 resistor"
- When modifying the libraries, notify the #electrical-git Slack channel 
- After creating a part in the library, request a review in the #electrical-part-review Slack channel

## Git Conflict Resolution
If you're updating a library or any binary file, and git tells you there is a conflict, please follow the following steps to resolve it:
1. Copy your local version somewhere else (ex. desktop)
2. Reset your changes
    - `git reset --hard`
3. Pull all the changes from the repository, overwriting your local copy
4. Make your changes in the updated version of the file
5. Commit and push your changes

If you made a lot of changes, or you suspect someone else is working on the same file as you at the same time, then you can check the change log on github.com, the app, or the terminal (git log) to see who made the most recent changes to the file.
