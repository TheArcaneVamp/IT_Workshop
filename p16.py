# <name>*<birth date>*<death date>
#separate into a list: list = ['<name>', '<birthdate>', '<death date>']
# further separate year from birth and death dates
# calculate years lived
record = "Soumen Mohapatro*1987-24-8*2024-04-01"
list = record.split('*')
born = list[1].split("-")
died = list[2].split("-")
print("Lived about", (int(died[0])-int(born[0])), "years")
