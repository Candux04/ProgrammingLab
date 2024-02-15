class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,window):
        self.window=window
        if type(self.window)!=int:
            try:
                self.window=int(self.window)
            except TypeError as e:
                raise ExamException('Tipo finestra non valido:{}'.format(e)) from e
        if self.window<1:
            raise ExamException('Finestra di lunghezza troppo piccola')

    def compute(self,a):
         if self.window==1:
             print(a)
             raise ExamException('Finestra di valore 1, media=valore')
         if a==[]:
             raise ExamException('Lista di valori vuoto')
         n=self.window-1
         lista=[]
     #    for n in a:
      #       x=a[n]
       #      try:
        #         x+1
         #    except:
          #       raise ExamException('Lista di valori con tipi non validi')
         if len(a)<self.window:
             raise ExamException('Finestra di lunghezza troppo grande')
         for i in range(len(a)-n):
             mean=0
             for p in range(self.window):
                 mean=mean+a[p+i]
             mean=mean/self.window
             lista.append(mean)
         return lista 



ma=MovingAverage(2)
r=ma.compute([2,4,8,16])
print(r)