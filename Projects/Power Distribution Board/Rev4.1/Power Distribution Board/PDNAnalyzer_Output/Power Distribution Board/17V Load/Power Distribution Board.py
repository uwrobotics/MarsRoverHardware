designFile = "C:/Users/farri/Documents/GitHub/MarsRoverHardware/Projects/Power Distribution Board/Rev3/PDNAnalyzer_Output/Power Distribution Board/odb.tgz"

powerNets = ["17V", "17V_LOAD"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("C28", "1") ],
"ground_pins": [ ("C28", "2") ],
"voltage": 17,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J13", "1") ],
"ground_pins": [ ("J13", "2") ],
"current": 4,
"Rpin": 0.025,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("U15", "3") ],
"out": [ ("U15", "5"), ("U15", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 6.66666666666667E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'MID_LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.5, 'Thickness': 0.001065},
        {'name': 'MID_LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
