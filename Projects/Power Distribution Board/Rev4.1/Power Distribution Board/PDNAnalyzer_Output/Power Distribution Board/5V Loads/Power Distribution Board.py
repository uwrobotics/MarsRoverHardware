designFile = "C:/Users/farri/Documents/GitHub/MarsRoverHardware/Projects/Power Distribution Board/Rev3/PDNAnalyzer_Output/Power Distribution Board/odb.tgz"

powerNets = ["5V", "5V_LOAD1", "5V_LOAD2", "5V_LOAD3", "5V_LOAD4"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("J10", "1") ],
"ground_pins": [ ("J10", "2") ],
"current": 2.5,
"Rpin": 0.04,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J11", "1") ],
"ground_pins": [ ("J11", "2") ],
"current": 2.5,
"Rpin": 0.04,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("J12", "1") ],
"ground_pins": [ ("J12", "2") ],
"current": 2.5,
"Rpin": 0.04,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("J14", "1") ],
"ground_pins": [ ("J14", "2") ],
"current": 2.5,
"Rpin": 0.04,
}
,
{
"id": "4",
"type": "source",
"power_pins": [ ("C78", "1") ],
"ground_pins": [ ("C78", "2") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "5",
"type": "source",
"power_pins": [ ("C79", "1") ],
"ground_pins": [ ("C79", "2") ],
"voltage": 5,
"Rpin": 0,
}
]


voltage_regulators = [
{
"id": "6",
"type": "linear",

"in": [ ("U6", "3"), ("U6", "2") ],
"out": [ ("U6", "7"), ("U6", "6"), ("U6", "5") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.084,
}
,
{
"id": "7",
"type": "linear",

"in": [ ("U7", "3"), ("U7", "2") ],
"out": [ ("U7", "7"), ("U7", "6"), ("U7", "5") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.084,
}
,
{
"id": "8",
"type": "linear",

"in": [ ("U8", "3"), ("U8", "2") ],
"out": [ ("U8", "7"), ("U8", "6"), ("U8", "5") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.084,
}
,
{
"id": "9",
"type": "linear",

"in": [ ("U10", "3"), ("U10", "2") ],
"out": [ ("U10", "7"), ("U10", "6"), ("U10", "5") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.084,
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
