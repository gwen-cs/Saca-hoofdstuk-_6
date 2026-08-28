a = b"Howest"
print(a)

ascii_string = "foobar"
non_ascii_string = " → "
print(f"{ascii_string=} {non_ascii_string=}")

ascii_bytes = ascii_string.encode("utf-8")
non_ascii_bytes = non_ascii_string.encode("utf-8")
print(f"{ascii_bytes=} {non_ascii_bytes=}")

print (ascii_bytes.decode('utf-8'))
print(non_ascii_bytes.decode('utf-8'))

# opvragen van bestanden (voor grote bestanden)

# with open("demo.txt", 'r') as fp:
#     content = fp.read()
#     # opened het document aan met de naam demo.txt en zet daar hele document in
#     content = fp.readline()
#     # opened het document aan met de naam demo.txt en zet daar de eerste regel in


# maakt een list van al de directory
import os

directory_content = os.listdir("./")
print(directory_content) # list
# vb. ['.idea', '.venv', 'demo.txt', 'main.py', 'README.md', 'testmap']


# print een lijst af regel per regel met de directory
import os

for rootdir, dirs, files in os.walk('.'): # walk is echt bedoeld om te gebruiken in een lus
    print(f"directory {rootdir} has {len(dirs)} subdirectories and {len(files)} files")

# vb
# directory .\.idea\inspectionProfiles has 0 subdirectories and 1 files
# directory .\.venv has 3 subdirectories and 3 files
# directory .\.venv\Include has 0 subdirectories and 0 files