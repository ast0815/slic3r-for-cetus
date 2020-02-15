import sys
import re
import tempfile
import os

print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ Adjusting extrusion lengths for Cetus printer +++
+++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

try:
    file = sys.argv[1]
    E = re.compile(r" E([-0-9.]+)")
    F = re.compile(r" F([-0-9.]+)")

    out = ""
    with open(file, 'r') as f:
        for line in f:
            match = E.search(line)
            if match:
                # Scale extrusion
                try:
                    new_E = float(match.group(1)) * 23.
                    line = re.sub(E, " E%f"%(new_E), line)
                except ValueError:
                    # Probably matched something that is not an E command
                    pass
                
                match = F.search(line)
                if match and 'X' not in line and 'Y' not in line and 'Z' not in line:
                    # Scale speed if there is no actual axis movement
                    try:
                        new_F = float(match.group(1)) * 23.
                        line = re.sub(F, " F%f"%(new_F), line)
                    except ValueError:
                        # Probably matched something that is not an E command
                        pass
            out += line
except Exception as e:
    print("Script failed!")
    print(e)
    input()
else:
    with open(file, 'w') as f:
        f.write(out)
