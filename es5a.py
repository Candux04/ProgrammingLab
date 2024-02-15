class CSVFile():
    def __init__(self,name):
       self.name=name
       try:
           my_file.open=('shampoo_sales.csv','r')
       except Exception as Errore:
           print('Errore: "{}"'.format(Errore))
        
    def get_data(self):
        list=[]
        #my_file=open('sahmpoo_sales.csv','r')
        for line in self.name:
            line=line.strip()
            elements=line.split(",")
            if elements[0]!='Date':
                list.append(elements)
        return list

#my_file='shampoo_sales.csv'
#file=CSVFile(my_file)
#print(file.get_data())



#var='25'
#try:
 #   var=float(var)
#except Exception as e:
 #   print('No gay')
  #  print('errore:"{}"\n"{}"\n"{}'.format(e,type(var),var))
#else:
 #   print('Daje Roma')
  #  print(var)
#finally:
 #   print('Era una barzelletta')
