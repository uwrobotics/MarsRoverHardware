# Mars Rover 2020 Hardware Repository
This repository contains:
- PCB design rules [[Design Rules](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Design%20Rules)]
- Altium libraries [[Library](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Library)]
- PCB designs [[Projects](https://github.com/uwrobotics/MarsRover2020-firmware/tree/alex/add-readme/misc)]
- Altium templates [[Templates](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Templates)]

Further descriptions and instructions for using each individual board are available in the README in the relevant board's directory.

## UWRT Hardware Development Instructions

1. Download [Diptrace](https://diptrace.com/download/download-diptrace/)
2. Complete the [555 timer PCB tutorial](https://docs.google.com/document/d/1YiGjYYuB-FUKcaG-C9Ers9Dd0e59WRM9QEbI4RcCCmw/edit?usp=sharing) in Diptrace
3. Request Altium license from [aascalon](https://github.com/aascalon)
4. Download [Altium Designer 19.1.9](https://www.altium.com/products/downloads/)
5. Download [Saturn PCB Toolkit](http://www.saturnpcb.com/pcb_toolkit/)
6. Clone repository
    - `git clone https://github.com/uwrobotics/MarsRover2020-PCB.git`
7. Read the [wiki](https://github.com/uwrobotics/MarsRover2020-PCB/wiki)

## Best Contribution Practices and Tips
- Preface your commit message with the project name. For example "Arm: add TVS diode" or "Library: add 10K 0603 resistor"
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
