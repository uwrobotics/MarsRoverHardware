designFile = "C:/Users/kyleh/Desktop/Works/UWRT/MarsRover2021-hardware/Projects/High Power Brushed Motor Controller/Rev1/PDNAnalyzer_Output/High Power Brushed DC MC/odb.tgz"

powerNets = ["24V", "MOTOR_M"]

groundNets = ["GND", "MOTOR_P"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("J3", "pdna_pin_2_1"), ("J3", "pdna_pin_2_2"), ("J3", "pdna_pin_2_3"), ("J3", "pdna_pin_2_4") ],
"ground_pins": [ ("J3", "pdna_pin_1_1"), ("J3", "pdna_pin_1_2"), ("J3", "pdna_pin_1_3"), ("J3", "pdna_pin_1_4") ],
"current": 26.5,
"Rpin": 0.0150943396226415,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("J2", "pdna_pin_1_1"), ("J2", "pdna_pin_1_2"), ("J2", "pdna_pin_1_3"), ("J2", "pdna_pin_1_4") ],
"ground_pins": [ ("J2", "pdna_pin_2_1"), ("J2", "pdna_pin_2_2"), ("J2", "pdna_pin_2_3"), ("J2", "pdna_pin_2_4") ],
"voltage": 24,
"Rpin": 0,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("Q4", "3") ],
"out": [ ("Q4", "pdna_pin_1_1"), ("Q4", "pdna_pin_1_2"), ("Q4", "pdna_pin_1_3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0024,
}
,
{
"id": "3",
"type": "linear",

"in": [ ("Q5", "pdna_pin_1_1"), ("Q5", "pdna_pin_1_2"), ("Q5", "pdna_pin_1_3") ],
"out": [ ("Q5", "3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0024,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 7E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GROUND', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.3, 'Thickness': 0.0014986},
        {'name': 'POWER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 7E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
