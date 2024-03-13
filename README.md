# Lightburn-config-for-Wazer-waterjet
This repository contains configuration files for LightBurn to get the WAZER waterjet working on LightBurn.

⚠️ **Warning! Use at your own risk.** ⚠️

So I have been working on getting my Wazer to work with LightBurn using the custom GCode device. I have also converted the materials library to a LightBurn library. The machine can be imported in the device’s menu and the library in the libraries panel.

I am still working on finetuning this but so far it’s working great!.

I plan to also directly control the Wazer using the USB port on the Smoothieboard.

![Untitled](https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/c7a7b379-587b-4bc7-90d8-d4cf26ec04f5)


<br><br>

**Machine**: (This file can be imported in the devices menu)

<img width="283" alt="Screenshot 2024-03-13 072137" src="https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/8a682772-a6c2-45a7-801e-5824b7fc3a2f">

To download this file hit ctrl+s on the page below and save it as **WAZER.lbdev**

https://raw.githubusercontent.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/main/WAZER.lbdev

<br>
<br>

**Material Library**: (This file can be loaded in the library panel)

<img width="297" alt="Screenshot 2024-03-13 072243" src="https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/4a274c95-1e48-4a53-af5d-2d961cdbc9d2">


To download this file hit ctrl+s on the page below and save it as **WAZER Library.clb**

https://raw.githubusercontent.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/main/WAZER%20Library.clb

<br><br>

The **Start from** option should be set to **Absolute Coords**

![image](https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/30138b4d-0b23-434f-8a53-c81e09e9b781)

<br><br>

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
<br>
The materials have lead ins enabled.
<br>
<img src="https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/5b154c51-493c-4823-b826-1d40a3a56619" width="500">

<br>
<br>
All Wazer Materials in a LightBurn Library.<br>
Select any material and hit the <b>Assign</b> button to apply the settings to the selected layer.
<br>
<img width="500" alt="Screenshot 2024-03-13 073206" src="https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/b23fe4e8-962e-433a-a459-4636fd166848">


<br>

Result.
<br>
<img src="https://github.com/ChrisAnd1998/Lightburn-config-for-Wazer-waterjet/assets/50437199/b7e4171c-f1e7-43e2-b2ad-6a3252418975" width="500">

