designFile = "C:/Users/Vladimir/Documents/GitHub/MarsRoverHardware/Projects/24V Multiphase Buck/Rev 2/PDNAnalyzer_Output/24V Multiphase Buck/odb.tgz"

powerNets = ["24V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("C19", "2") ],
"ground_pins": [ ("C19", "1") ],
"voltage": 24,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J2", "pdna_pin_1_1"), ("J2", "pdna_pin_1_2") ],
"ground_pins": [ ("J2", "pdna_pin_2_1"), ("J2", "pdna_pin_2_2") ],
"current": 15,
"Rpin": 0.0133333333333333,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'L3_-_POWER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'L2_-_GND', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOT', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
