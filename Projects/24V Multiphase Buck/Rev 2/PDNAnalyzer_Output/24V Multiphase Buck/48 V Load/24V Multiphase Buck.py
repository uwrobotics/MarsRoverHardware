designFile = "C:/Users/Vladimir/Documents/GitHub/MarsRoverHardware/Projects/24V Multiphase Buck/Rev 2/PDNAnalyzer_Output/24V Multiphase Buck/odb.tgz"

powerNets = ["VBAT"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "pdna_pin_1_1"), ("J1", "pdna_pin_1_2") ],
"ground_pins": [ ("J1", "pdna_pin_2_1"), ("J1", "pdna_pin_2_2") ],
"voltage": 48,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("Q1", "2") ],
"ground_pins": [ ("Q3", "3") ],
"current": 8.8,
"Rpin": 0.0113636363636364,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("Q5", "2") ],
"ground_pins": [ ("Q7", "3") ],
"current": 8.8,
"Rpin": 0.0113636363636364,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'MID_LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.5, 'Thickness': 0.001265},
        {'name': 'MID_LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
