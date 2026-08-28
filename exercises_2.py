# oefening 2
#***********

with open ("input.txt", "r") as input_file:
    regels = input_file.readlines()

output_file = open("output.txt", "w")

for regel in regels:
    output_file.write(regel.upper())

output_file.close()
