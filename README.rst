================
slic3r-for-cetus
================

Configuration and supporting scripts for Slic3r and Cetus Mk II

Setup Instructions
==================

1.  Import the configuration into Slic3r
2.  Change the configuration so it finds the post-processing sctipt (you need a working Python setup)
3.  Use Up-Studio to determine the z-offset of the z-axis stop
4.  Update the printer start gcode with that value

Print Instructions
==================

1.  Slice an STL, export gcode
2.  Connect Up-Studio to the printer
3.  Initialise printer in Up-Studio before each print!
4.  Add gcode file to Up-Studio instead of STL

Explanations
============

The Slic3r configuration should produce gcode that is almost usable with the printer.
Only the extrusion distances are off by a large factor.
This is fixed by the post-processing script.
