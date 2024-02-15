#SBAGLIATA
class NumericalCSVFile():
    def __init__(self,name):
       self.name=name
       
    def get_data(self):
        list=[]
        #my_file=open('sahmpoo_sales.csv','r')
        for line in self.name:
            try:
                line=float(line)
            except Exception as e:
                print('Errore: "{}"'.format(e))
            line=line.strip()
            elements=line.split(",")
            if elements[0]!='Date':
                list.append(elements)
        return list

#my_file=open('shampoo_sales2.csv','r')
#file=NumericalCSVFile(my_file)
#print(file.get_data())

    