designFile = "C:/UWRT/MarsRover2020-PCB/Projects/Low Power Brushed Motor Controller/Rev1/PDNAnalyzer_Output/Low Power Brushed Motor Controller/odb.tgz"

powerNets = ["12V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "3") ],
"ground_pins": [ ("J1", "4") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("Q1", "2") ],
"ground_pins": [ ("GND", "1") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'GND', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': '12V_FUSED', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
