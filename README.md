# Lightburn-config-for-Wazer-waterjet
This repository contains configuration files for LightBurn to get the WAZER waterjet working on LightBurn.

⚠️ **Warning! Use at your own risk.** ⚠️

So I have been working on getting my Wazer to work with LightBurn using the custom GCode device. I have also converted the materials library to a LightBurn library. The machine can be imported in the device’s menu and the library in the libraries panel.

I am still working on finetuning this but so far it’s working great!.

USB Communication works except pressure valve and abrasive valve commands.
It seems the Wazer needs to run through its safety screen before the pressure valve and abrasive valve can be controlled.
So for now you can do a dry run and if it's correct you can put the gcode file on you SD card.

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

Below is an explanation and dissection of the WAZER G-code structure so that you can understand how WAZER is interpreting the series of commands that Wam generates. These are all critical for your WAZER to function corrrectly and safely:

Cut File Parameters - This section contains all the parameters selected in WAM for generating the cut file. These parameters are for reference only and changing these would not affect the cut.
```
G90 - Absolute Mode: All of your coordinates and movements are referenced from the top left corner of the cutting area. This is why the WAZER goes through the homing routine at the start of your. The WAZER controller does NOT support any other modes besides G90 (absolute).
G21 - Millimeter mode: All coordinates will be interpreted as millimeters. We recommend to keep this as this is the default for WAM. The WAZER controller does NOT support any other modes besides G21 (mm).
M1403 - WAZER Initialization: This calls critical startup subroutines built into the WAZER firmware that allow it to correctly function.
M1405 X##.## Y##.## - This defines the bounding box top left corner used in the “Cut Extents” option before a cut. This aids you in making sure that the cut will be correctly located on your material.
M1406 X##.## Y##.## - This defines the bounding box bottom right corner used in the “Cut Extents” option before a cut. This aids you in making sure your cut will fit on your material.
M1407 S##.# - This defines the re-pierce time after a pause or unexpected stoppage.
M1410 #.#; Generated on Wam - This lets the firmware know which version of Wam the g-code was generated with. This assures compatibility between the version of Wam you generated your G-code file with and the current version of your WAZER machine firmware. This is critical, as the M-codes we use can change over time as well as how the firmware interprets them.
M1411 Material Name - This lets the firmware know what material was selected during the cut file generation. This parameter is read by the firmware and displayed on screen for users reference when a cut file is selected.
M1412 Material Thickness - This lets the firmware know what material thickness was selected during the cut file generation. This parameter is read by the firmware and displayed on screen for users reference when a cut file is selected.
G0 X#.## Y-#.## - Rapid movement. This will move the the specified coordinates at the predefined rapid speed.
G1 X#.## Y#.## F##.## - Move to specified coordinates at the speed of F#.## (in mm/min)
M3 - Opens the high pressure valve
M5 - Closes the high pressure valve
M8 - Opens the abrasive valve - this starts the flow of abrasive
M9 - Closes the abrasive valve
G4 S##.# - Pause for S##.# seconds. This is used in multiple occasions throughout the G-code file. It can function as a:
pierce time
dynamic catchup for the jet to produce a cleaner cut on your part
required delay between on/off or off/on of certain peripherals due to the machine’s dynamics
a method to ensure safe operation and shutdown of components
M1413 HH:MM:SS - This lets the firmware know the expected cut time for the given cut. This parameter is also read and displayed after the file is selected for users reference.
M1404 - WAZER shutdown: This calls critical shut down subroutines built into the WAZER firmware that allow it to correctly function.
```
<br>
Extra commands found in firmware.bin

```
M1400: Provides help/information about available commands.
M1401: Enables a specific module.
M1402: Stops a specific module.
M1403: Required at the start of the stream of G-codes to turn on the water and abrasive.
M1404: Required at the end of the stream of G-codes to turn off the water and abrasive.
M1405: Generated by the host to specify the bounded box top left point.
M1406: Generated by the host to specify the bounded box bottom right point.
M1407: Sets a dwell period in integer seconds to enable the waterjet cutter to pierce the material.
M1408: Turns on debug messages.
M1409: Turns off debug messages.
```


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

