#mayusculas primera letra
name="angel sainero"
print (name.title())
#ngel Sainero

#--------------------------------------------------------------------------------------
#cambia a mayusculas y minusculas
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
#ADA LOVELACE
#ada lovelace

#-----------------------------------------------------------------------------------------
#uso de f
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
#Hello, Ada Lovelace!

#-----------------------------------------------------------------------------------------
#uso de format
first_name = "ada"
last_name = "lovelace"
full_name = "{} {}".format (first_name, last_name)
message = "Hello, {}!" .format (full_name.title())
print(message)
#Hello, Ada Lovelace!

#--------------------------------------------------------------------------------------------
#tabulaciones y espacios en blanco 
