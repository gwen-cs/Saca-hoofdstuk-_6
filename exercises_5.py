import os
from pathlib import Path

demo = "demo"

if not os.path.exists(demo):
    os.mkdir(demo)

course1 = os.path.join(demo, "course1")
course2 = os.path.join(demo, "course2")

if not os.path.exists(course1):
    os.mkdir(course1)

if not os.path.exists(course2):
    os.mkdir(course2)

bestand1 = Path(course1) / "voorbeeld.txt"
bestand2 = Path(course2) / "voorbeeld.txt"

bestand1.write_text("Dit is een voorbeeldbestand van course1.")
bestand2.write_text("Dit is een voorbeeldbestand van course2.")

print("Mappen en bestanden zijn aangemaakt.")