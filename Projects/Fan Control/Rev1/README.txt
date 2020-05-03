ALERT/TACH (Pin 6) configuration:
If Pin 6 is configured as TACH input, then it will not respond to the ARA command and error conditions will not tirgger interrupt.
To check error conditions with TACH as input, read STATUS REGISTER.

If Pin 6 is configured as Interrupt, it is raised high whenever an out of limit temperature is detected. Must be cleared manually.

Mask Bit:


Power Modes:

Normal: TEMP and FAN DRIVER both active, monitors TEMP and checks FAN CONTROL LOOK-UP table.
Standby: 1-shot command refreshes TEMP, FAN DRIVER on default drive. Refersehed TEMP is checked against TLIMIT not FAN CONTROL LOOK-UP.
Mixed: 1-shot command refreshes TEMP, FAN DRIVER is active. Refreshed TEMP is checked against FAN CONTROL LOOK-UP.

