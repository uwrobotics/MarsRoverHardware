# MarsRover2019-PCB
Contains schematics and PCB designs

Conflict Resolution
If you're updating a library or any binary file, and git tells you there is a conflict, please follow the following steps to resolve it:
1. Copy your local version somewhere else (ex. desktop).
2. Undo your changes.
3. Pull all the changes from the repository, overwriting your local copy.
4. Make your changes in the updated version of the file.
5. Commit and push your changes.

If you made a lot of changes, or you suspect someone else is working on the same file as you at the same time, then you can check the change log on github.com, the app, or the terminal (git log) to see who made the most recent changes to the file.

# Folder structure
In the Projects folder, make a folder for your board. Under it should be folders for each revision. 
Within each revision, the following structure should be observed:
- Board.PrjPCB (The project file for your PCB)
- Board.OutJob (Output Job File for your PCB)
- sch (folder containing your schematic sheets)
- pcb (folder containing your .PcbDoc)
- fab (folder with BOM and Gerber files)
- assy (folder containing assembly drawing and STEP file)
