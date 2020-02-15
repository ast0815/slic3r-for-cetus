import sys
import re
import tempfile
import os

print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ Adjusting extrusion lengths for Cetus printer +++
+++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

file = sys.argv[1]
E = re.compile(r" E([-0-9.]+)")
F = re.compile(r" F([-0-9.]+)")

out = ""
with open(file, 'r') as f:
    for line in f:
        match = E.search(line)
        if match:
            # Scale extrusion
            new_E = float(match.group(1)) * 23.
            line = re.sub(E, " E%f"%(new_E), line)
            match = F.search(line)
            if match and 'X' not in line and 'Y' not in line and 'Z' not in line:
                # Scale speed if there is no actual axis movement
                new_F = float(match.group(1)) * 23.
                line = re.sub(F, " F%f"%(new_F), line)
        #print(line, end='')
        out += line

with open(file, 'w') as f:
    f.write(out)
