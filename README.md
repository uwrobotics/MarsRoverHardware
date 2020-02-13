# Mars Rover 2020 Hardware Repository
This repository contains:
- Designs from previous years [[2019 Projects](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/2019%20Projects)]
- Tutorial submissions [[555 Timer Tutorial](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/555%20Timer%20Tutorial)]
- Bringup code [[Bringup Firmware](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Bringup%20Firmware/GPIO%20Test)]
- PCB design rules [[Design Rules](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Design%20Rules)]
- Altium libraries [[Library](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Library)]
- PCB designs [[misc](https://github.com/uwrobotics/MarsRover2020-firmware/tree/alex/add-readme/misc)]
- Altium templates [[Templates](https://github.com/uwrobotics/MarsRover2020-PCB/tree/master/Templates)]

Further descriptions and instructions for using each individual board are available in the README in the relevant board's directory.

## UWRT Hardware Development Instructions

1. Download [Diptrace](https://diptrace.com/download/download-diptrace/)
2. Complete the 555 timer PCB tutorial in Diptrace(https://docs.google.com/document/d/1YiGjYYuB-FUKcaG-C9Ers9Dd0e59WRM9QEbI4RcCCmw/edit?usp=sharing)
3. Request Altium license from [aascalon](https://github.com/aascalon)
4. Download [Altium Designer 19.1.9](https://www.altium.com/products/downloads/)
5. Download [Saturn PCB Toolkit](http://www.saturnpcb.com/pcb_toolkit/)
6. Clone repository
7. Read the wiki

## Best Contribution Practices and Tips

## Git Conflict Resolution
If you're updating a library or any binary file, and git tells you there is a conflict, please follow the following steps to resolve it:
1. Copy your local version somewhere else (ex. desktop)
2. Undo your changes
3. Pull all the changes from the repository, overwriting your local copy
4. Make your changes in the updated version of the file
5. Commit and push your changes

If you made a lot of changes, or you suspect someone else is working on the same file as you at the same time, then you can check the change log on github.com, the app, or the terminal (git log) to see who made the most recent changes to the file.
