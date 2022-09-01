designFile = "C:/Users/Vladimir/Documents/GitHub/MarsRoverHardware/Projects/24V Multiphase Buck/Rev 2/PDNAnalyzer_Output/24V Multiphase Buck/odb.tgz"

powerNets = ["24V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("R3", "2") ],
"ground_pins": [ ("C19", "1") ],
"voltage": 24,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J2", "pdna_pin_1_2"), ("J2", "pdna_pin_1_1") ],
"ground_pins": [ ("J2", "pdna_pin_2_2"), ("J2", "pdna_pin_2_1") ],
"current": 30,
"Rpin": 0.00666666666666667,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("R10", "2") ],
"ground_pins": [ ("C26", "1") ],
"voltage": 24,
"Rpin": 0,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05},
        {'name': 'TOP', 'Conductivity': 47000000, 'Thickness': 7.501E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'PWR', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.5, 'Thickness': 0.001065},
        {'name': 'GND', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'BOT', 'Conductivity': 47000000, 'Thickness': 7.501E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
