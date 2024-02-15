""""def sum_csv(file):
    lista=[]
    for line in file:
        elements=line.split(',')
        if elements[0]!= 'Date':
            date=elements[0]
            valori=float(elements[1])
            lista.append(valori)
    return sum(lista)

file=open('shampoo_sales.csv', 'r')

print(sum_csv(file))
"""""
class Persona():
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome

persona = Persona('Francesco','Mastrovito')
print(persona)
print(persona.nome)
print(persona.cognome)