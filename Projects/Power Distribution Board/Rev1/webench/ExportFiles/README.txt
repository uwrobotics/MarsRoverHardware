## WEBENCH Design 13
Created at Wed May 20 19:43:34 PDT 2020
**********************************************************
***************** Schematic Instructions  ****************
**********************************************************

To import your new Schematic into Altium:

1. Unzip the downloaded folder files to a local directory and 
   Start the Altium program.
2. From the menu select "File"->"Open".
3. Select the file named in the path above ending with ".schdoc"
   and "Open" the file.
4. Your Schematic should be viewable within Altium now.

For additional information, please visit this site:
http://www.accelerated-designs.com/help/Altium_BrdSch_import.html



**********************************************************
*******************  PCB Instructions  *******************
**********************************************************


To import your new BOARD into Altium:

1. Unzip the downloaded folder files to a local directory
	and Start the Altium program.
2. From the menu select "File"->"Open".
3. Select the file named in the path above ending with ".pcbdoc"
   and "Open" the file.
4. Planes will need to be repoured to update the Copper Pour Polygons
	a. Once your board is loaded, select the Tools menu from the
	   top Menu Bar
	b. Scroll to the Polygon Pours item on the Tools Menu.
	c. The Polygon Pours item should expand to show more options
	d. Select Repour All Polygons, this will repour all of the
	   polygons.
5. Your board should be viewable within Altium now.

For additional information, please visit this site:
http://www.accelerated-designs.com/help/Altium_BrdSch_import.html

**********************************************************
*******************  LIB Instructions  *******************
**********************************************************

To import your new LIBRARY PARTS into Altium follow these steps:

1. After running the Ultra Librarian export for the first time,
   you will need to copy the following files into an area where
   they can be accessed for all future translations.  They are script
   files that Altium will need to be able to find.
	a. UL_Form.dfm
	b. UL_Form.pas
	c. UL_Import.pas
	d. UL_Import.prjScr
2. The above script file will need to be run from within Altium.
   This can be done by going to File, Open and selecting the
   UL_Import.PrjScr file stored above.
3. Select the "DXP" dropdown menu in the top-left corner runfrom
   the drop down menu and select "Run Script". Select "UL_Form.pas"
   and click "OK"
4. When the script is run, it will ask you for the file name of the
   Ultra Librarian file to run. Click "File...", select the latest file
   produced with a date code (for instance 2010-02-17_23-12-34.txt), and
   click "Start Import".
5. The script will open a new Integraged Library project and import
   the Ultra Librarian data into it.  When complete a message box
   will pop up saying that import is done.

For additional information, please visit this site:
http://www.accelerated-designs.com/help/Altium_import.html

For a video tutorial, please visit:
http://youtu.be/pih50yx9HYU

**********************************************************
****************  SIMULATION Instructions  ***************
**********************************************************
This XML can be imported in Altium Designer 14 and higher using
WEBENCH Altium Connector Extension and simulated using WEBENCH
Simulation Engine.

The WEBENCH Altium Connector provides an interface to the
Texas Instruments WEBENCH Designer Tools as well as to open
WEBENCH exported Designs directly from inside Altium Designer.
It also includes the advanced WEBENCH Simulation Engine which
can be used for offline circuit simulations.

You will need to activate WEBENCH Altium Connector to be able
to use the WEBENCH Simulation Engine.

Installation guide:
http://www.ti.com/lit/SNVU481
You can download the WEBENCH extension from Altium Designer Extensions.

Connector Details:
http://www.ti.com/lsds/ti/analog/webench/altiumconnector.page

More about WEBENCH simulation export to Altium:
http://www.ti.com/lsds/ti/analog/webench/simexportaltium.page

User Manual:
http://www.ti.com/lit/szzu007

