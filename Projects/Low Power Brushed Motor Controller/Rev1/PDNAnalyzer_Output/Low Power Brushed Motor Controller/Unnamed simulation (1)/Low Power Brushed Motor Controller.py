designFile = "C:/Users/kyleh/Desktop/Works/UWRT/MarsRover2020-PCB/Projects/Low Power Brushed Motor Controller/Rev1/PDNAnalyzer_Output/Low Power Brushed Motor Controller/odb.tgz"

powerNets = ["OUTA", "12V_FUSED"]

groundNets = ["OUTB", "GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("U1", "2"), ("U1", "15") ],
"ground_pins": [ ("U1", "7"), ("U1", "10") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("OUTA", "1") ],
"ground_pins": [ ("OUTB", "1") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("F1", "2") ],
"ground_pins": [ ("GND", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("U1", "4"), ("U1", "5"), ("U1", "12") ],
"ground_pins": [ ("U1", "1"), ("U1", "8"), ("U1", "16"), ("U1", "9") ],
"current": 7,
"Rpin": 0.0489795918367347,
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
