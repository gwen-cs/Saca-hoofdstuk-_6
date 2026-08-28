# enkel voor linux !!
#********************
import os

import subprocess

print("Process ID:", os.getgid())
print("User ID:", os.getuid())
print("Group ID:", os.getgid())

os.environ ["MIJN VARIABELE"] = "Hallo Gwen"

subprocess.run(["printenv", "MIJN VARIABELE"])
