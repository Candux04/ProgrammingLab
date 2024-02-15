class CSVFile:
    
    def __init__(self,name):
        self.name=name
        try:
            type(self.name)==string
        except Exception as e:
            print('nome del file non stringa: {}',type(self.name))
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        
    def get_data(self, start=0, end=4):
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None
        else:
            data=[]
            my_file=open(self.name,'r')
            for line in my_file:
                elements=line.split(',')
                elements[-1]=elements[-1].strip()
                if elements[0]!='Date':
                    data.append(elements)
                    start=start+1
                if start>=end:
                    break
        my_file.close
        return data
            
mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data()))
