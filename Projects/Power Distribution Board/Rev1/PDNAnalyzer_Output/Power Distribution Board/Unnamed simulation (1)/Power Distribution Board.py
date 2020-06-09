designFile = "C:/Users/kyleh/Desktop/Works/UWRT/MarsRover2021-hardware/Projects/Power Distribution Board/Rev1/PDNAnalyzer_Output/Power Distribution Board/odb.tgz"

powerNets = ["VBAT", "NetD2_2", "VBAT_FUSED", "+IN", "+OUT", "5V", "SW", "17V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 24,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J9", "1") ],
"ground_pins": [ ("J2", "2") ],
"current": 8,
"Rpin": 0.0125,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("J5", "1") ],
"ground_pins": [ ("J5", "2") ],
"current": 1.65,
"Rpin": 0.0606060606060606,
}
,
{
"id": "3",
"type": "source",
"power_pins": [ ("U1", "A'"), ("U1", "C'") ],
"ground_pins": [ ("U1", "E"), ("U1", "B'"), ("U1", "D'") ],
"voltage": 5,
"Rpin": 0.006,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U1", "A") ],
"ground_pins": [ ("U1", "E"), ("U1", "B'"), ("U1", "D'") ],
"current": 3.72534690959421,
"Rpin": 0.04026470652,
}
,
{
"id": "5",
"type": "source",
"power_pins": [ ("U2", "8") ],
"ground_pins": [ ("U2", "9"), ("U2", "7") ],
"voltage": 17,
"Rpin": 0.00333333333333333,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U2", "2") ],
"ground_pins": [ ("U2", "9"), ("U2", "7") ],
"current": 1.23989081427295,
"Rpin": 0.107536350619323,
}
]


voltage_regulators = [
{
"id": "7",
"type": "linear",

"in": [ ("Q1", "2") ],
"out": [ ("Q1", "3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.00565,
}
,
{
"id": "8",
"type": "linear",

"in": [ ("F1", "1") ],
"out": [ ("F1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.002525,
}
,
{
"id": "9",
"type": "linear",

"in": [ ("L1", "1") ],
"out": [ ("L1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 7.8E-05,
}
,
{
"id": "10",
"type": "linear",

"in": [ ("L2", "1") ],
"out": [ ("L2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0065,
}
,
{
"id": "11",
"type": "linear",

"in": [ ("L3", "1") ],
"out": [ ("L3", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0065,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.3, 'Thickness': 0.00012954},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.3, 'Thickness': 0.00012954},
        {'name': 'INT1__GND_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.8, 'Thickness': 0.0007112},
        {'name': 'INT2__PWR_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-4', 'DielectricConstant': 4.3, 'Thickness': 0.00012954},
        {'name': 'SUBSTRATE-5', 'DielectricConstant': 4.3, 'Thickness': 0.00012954},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
