from subprocess import run

cmd = ["openssl", "req", "-new", "-x509", "-nodes",
       "-out", "c.crt", "-keyout", "c.key"]

inp = ["BE", "West-Flanders", "Bruges", "Howest",
       "CS", "Saca", "saca@howest.be", "\n"]

res = run(cmd, input="\n".join(inp), text=True)