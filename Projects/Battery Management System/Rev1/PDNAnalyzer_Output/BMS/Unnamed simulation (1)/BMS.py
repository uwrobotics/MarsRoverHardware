designFile = "C:/Users/ayesh/Documents/GitHub/MarsRover2020-PCB/Projects/Battery Management System/Rev1/PDNAnalyzer_Output/BMS/odb.tgz"

powerNets = ["VBAT", "VBAT_FETS", "PACK+"]

groundNets = ["GND", "PACK-"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("J2", "pdna_pin_2_1"), ("J2", "pdna_pin_2_2"), ("J2", "pdna_pin_2_3"), ("J2", "pdna_pin_2_4") ],
"ground_pins": [ ("J2", "pdna_pin_1_1"), ("J2", "pdna_pin_1_2"), ("J2", "pdna_pin_1_3"), ("J2", "pdna_pin_1_4") ],
"current": 200,
"Rpin": 0.002,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("J3", "1") ],
"ground_pins": [ ("J3", "2") ],
"voltage": 25.2,
"Rpin": 0,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("Q3", "pdna_pin_2_1"), ("Q3", "pdna_pin_2_2"), ("Q3", "pdna_pin_2_3"), ("Q3", "pdna_pin_2_4"), ("Q3", "pdna_pin_2_5"), ("Q3", "pdna_pin_2_6"), ("Q3", "pdna_pin_2_7") ],
"out": [ ("Q3", "pdna_pin_3_1"), ("Q3", "pdna_pin_3_2"), ("Q3", "pdna_pin_3_3"), ("Q3", "pdna_pin_3_4") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.54545454545455E-06,
}
,
{
"id": "3",
"type": "linear",

"in": [ ("Q6", "pdna_pin_3_1"), ("Q6", "pdna_pin_3_2"), ("Q6", "pdna_pin_3_3"), ("Q6", "pdna_pin_3_4") ],
"out": [ ("Q6", "pdna_pin_2_1"), ("Q6", "pdna_pin_2_2"), ("Q6", "pdna_pin_2_3"), ("Q6", "pdna_pin_2_4"), ("Q6", "pdna_pin_2_5"), ("Q6", "pdna_pin_2_6"), ("Q6", "pdna_pin_2_7") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.54545454545455E-06,
}
,
{
"id": "4",
"type": "linear",

"in": [ ("R44", "1") ],
"out": [ ("R44", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GROUND', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'POWER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
