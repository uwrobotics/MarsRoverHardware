designFile = "C:/UWRT/MarsRover2021-hardware/Projects/Power Distribution Board/Rev2/PDNAnalyzer_Output/Power Distribution Board/odb.tgz"

powerNets = ["VBAT", "VBAT_FUSED", "24V", "17V", "5V"]

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
"power_pins": [ ("F1", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 5,
"Rpin": 0.02,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("Q1", "8") ],
"ground_pins": [ ("C1", "2") ],
"voltage": 24,
"Rpin": 0,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("Q2", "1") ],
"ground_pins": [ ("C6", "2") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U3", "2") ],
"ground_pins": [ ("U3", "7"), ("U3", "9") ],
"current": 1.65,
"Rpin": 0.0808080808080808,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("J2", "1") ],
"ground_pins": [ ("J2", "2") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U4", "A") ],
"ground_pins": [ ("U4", "E"), ("U4", "B'"), ("U4", "D'") ],
"current": 4,
"Rpin": 0.0375,
}
,
{
"id": "7",
"type": "source",
"power_pins": [ ("Q3", "1") ],
"ground_pins": [ ("C3", "2") ],
"voltage": 24,
"Rpin": 0,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("J5", "1") ],
"ground_pins": [ ("J5", "2") ],
"current": 1.65,
"Rpin": 0.0606060606060606,
}
,
{
"id": "9",
"type": "source",
"power_pins": [ ("L2", "2") ],
"ground_pins": [ ("C30", "1") ],
"voltage": 17,
"Rpin": 0,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("U15", "1"), ("U15", "8") ],
"ground_pins": [ ("U15", "6"), ("U15", "9") ],
"current": 1.65,
"Rpin": 0.121212121212121,
}
,
{
"id": "11",
"type": "source",
"power_pins": [ ("L3", "2") ],
"ground_pins": [ ("C40", "1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("U6", "1"), ("U6", "8") ],
"ground_pins": [ ("U6", "6"), ("U6", "9") ],
"current": 0.985,
"Rpin": 0.203045685279188,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("U8", "1"), ("U8", "8") ],
"ground_pins": [ ("U8", "6"), ("U8", "9") ],
"current": 1,
"Rpin": 0.2,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("U10", "1"), ("U10", "8") ],
"ground_pins": [ ("U10", "6"), ("U10", "9") ],
"current": 1,
"Rpin": 0.2,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("U7", "1"), ("U7", "8") ],
"ground_pins": [ ("U7", "6"), ("U7", "9") ],
"current": 1,
"Rpin": 0.2,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'SIGNAL', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GROUND_1', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'POWER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GROUND_2', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
