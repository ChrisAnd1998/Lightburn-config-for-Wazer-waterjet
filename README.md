# Lightburn-config-for-Wazer-waterjet
This repository contains configuration files for LightBurn to get the WAZER waterjet working on LightBurn.

So I have been working on getting my Wazer to work with LightBurn. Using the custom GCode device and converted the materials library to a LightBurn library. The machine can be imported in the device’s menu and the library in the libraries panel.

I am still working on finetuning this but so far it’s working great!

Machine:
https://raw.githubusercontent.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/main/WAZER.lbdev

Material Library:
https://raw.githubusercontent.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/main/WAZER%20Library.clb

The **Start from** option should be set to **Absolute Coords**

GCode generated with LightBurn:
(Rectangle with lead in)

```
M1403
M1405 X0.00 Y-0.00
M1406 X1.00 Y-10.00
M1407 S1.0
M1410 1.5
M1411 LightBurn
M1412 Gcode
G00 G17 G40 G21 G54
G90
G4 S1.
M9
G4 S1.
M5
G4 S1.
G0 X36.817Y-14.817
M3
M8
G4 S3.
G1 X37.142Y-14.833F89.16
G1 X37.458Y-14.882
G1 X37.763Y-14.96
G1 X38.056Y-15.067
G1 X38.334Y-15.201
G1 X38.597Y-15.361
G1 X38.842Y-15.544
G1 X39.068Y-15.749
G1 X39.273Y-15.975
G1 X39.456Y-16.22
G1 X39.616Y-16.483
G1 X39.75Y-16.761
G1 X39.857Y-17.053
G1 X39.935Y-17.358
G1 X39.984Y-17.675
G1 X40Y-18
G1 Y-60
G1 X102
G1 Y-18
G1 X40
G4 S1.
M9
G4 S1.
M5
G4 S1.
G90
M1413 00:00:00
M1404
```

The materials have lead ins enabled.

![037dd67536477b468ced65f69f9b696a55240d8a_2_967x750](https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/ff8ad663-94a4-413c-9d69-d2ccbacbdf9a)
![c95de87f333fa29ef905e28e1cd9a190d59c0b34_2_630x750](https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/8704d7a1-8c5c-4bd2-9619-49cb0e44bd0a)

