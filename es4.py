class CSVFile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        my_file=open(self.name,'r')
        list=[] #creo una lista
        
        for line in my_file:
            elements=line.strip().split(',') #stacco date da sales
            if elements[0]!='Date':
                list.append(elements) #aggiungo il valore alla lista
                
        return list
    
my_file=open('shampoo_sales2.csv')
file=CSVFile(my_file)
print(file.get_data())