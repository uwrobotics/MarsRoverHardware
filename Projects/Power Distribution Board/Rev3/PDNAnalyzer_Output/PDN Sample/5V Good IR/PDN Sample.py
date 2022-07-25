designFile = "C:/Users/farri/Documents/GitHub/MarsRoverHardware/Projects/Power Distribution Board/Rev3/PDNAnalyzer_Output/PDN Sample/odb.tgz"

powerNets = ["5V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("pdna_comp_5V_IN_3", "2") ],
"ground_pins": [ ("pdna_comp_5V_IN_3", "1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("pdna_comp_5V_OUT_2", "2") ],
"ground_pins": [ ("pdna_comp_5V_OUT_2", "1") ],
"current": 5,
"Rpin": 0.02,
}
]


voltage_regulators = []


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
