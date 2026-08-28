# oefening 1
#***********
string = "dit naar utf-8"
onmogelijke_string = "café"

# string omzetten naar utf-8
nieuwe_string = string.encode("utf-8")
nieuwe_onmogelijke_string = onmogelijke_string.encode("utf-8")

print("string omzetten naar utf-8")
print (nieuwe_string)
print (nieuwe_onmogelijke_string)

originele_string = nieuwe_string.decode("utf-8")
originele_onmogelijke_string = nieuwe_onmogelijke_string.decode("utf-8")
print ("\n")
print("utf-8 omzetten naar string")
print (originele_string)
print(originele_onmogelijke_string)

