class CSVFile():
    def __init__(self,name):
        self.name=name
    def get_data(self):
        valori=[]
        try:
            my_file=open(self.name,'r')
        except NameError as e:
            print("Errore:{}".format(e))