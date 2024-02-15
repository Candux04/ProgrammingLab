class Model():
    data=[50,52,60]
    def fit(self,data):
        raise NotImplementedError('Metodo non imp')
    def predict(self,data):
        raise NotImplementedError('Metodo non imp')


class TrendModel(Model):
    def predict(self,data):
        if len(data)!=4:
            raise ValueError('Passati troppi valori')
        var=[]
        prev=None
        for item in data:
            if prev is not None:
                var.append(item-prev)
            prev=item
        avg=sum(var)/len(var)
        pred=data[-1]+avg
        return pred
class FitTrendModel(TrendModel) :
    def fitavg(self,data):
        avv=super().predict
        avv=avv-data[-1]
        avgvar=[]
        prev=None
        for item in data:
            if prev is not None:
                avgvar.append(item-prev)
            prev=item
        va=sum(avgvar)/(len(avgvar))
        va=(va+avv)/2
        








#class CSVFile():
#    def __init__(self,name):
 #       self.name=name
#
 #   def get_data(self):
  #      list=[]
   #     for line in self.name:
    #        line=line.strip()
     #       elements=line.split(",")
      #      if elements[0]!='Date':
       #         value=float(elements[1])
        #        list.append(value)
        #return list
    
#class TrendModel(CSVFile):
 #       
  #  def predict(self,list):
   #     n=0
    #    diff=0
     #   j=1
      #  i=0
       # for item in list:
        #    n=n+1
         #   diff=diff+(item[j]-item[i])
          #  j=j+1
           # i=i+1
            
            
        #prediction=diff/n
        #return prediction

#my_file=open('shampoo_sales2.csv','r')
#file=TrendModel(my_file)
#print(file.predict)
