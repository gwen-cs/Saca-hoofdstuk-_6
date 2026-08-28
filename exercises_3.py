import os

for rootdir, dirs, files in os.walk("."):
    for file in files:

        pad = os.path.join(rootdir, file)

        grootte = os.path.getsize(pad)

        if grootte > 1024:

            print(file, grootte, "bytes")
            
