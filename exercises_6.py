import os
import subprocess

for rootdir, dirs, files in os.walk("."):

    if".git" in dirs:
        print("git repository  gevonden, rootdir")

        resultaat = subprocess.run(
            ["git", "log", "--oneline"],
            cwd=rootdir,
            capture_output=True,
            text=True
        )

        commits = resultaat.stdout.splitlines()

        print("Aantal commits:", len(commits))
        print(commits)