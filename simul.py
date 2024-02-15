class ExamException(Exception):
    pass
    
class MovingAverage():
    def __init__(self,fin):
        self.fin=fin
        if type(self.fin)!=int:
            try: 
                self.fin=int(self.fin)
            except TypeError as e:
                raise ExamException('Fin di tipo {} non numerabile'.format(e)) from e
        if self.fin<=1:
            raise ExamException('Finestra troppo piccola')
    def compute(self,a):
        if len(a)==0:
            raise ExamException('Array vuoto')
        for j in range(len(a)):
            if type(a[j])!=int:
                try:
                    a[j]=float(a[j])
                    a[j]=int(a[j])
                except ValueError as e:
                    raise ExamException('Array di valori non int') from e
        n=self.fin-1
        lista=[]
        if len(a)<self.fin:
            raise ExamException('Array troppo corto')
        for i in range(len(a)-n):
            media=0
            for p in range(self.fin):
                media=media+a[p+i]
            media=media/self.fin
            lista.append(media)
        return lista


ma=MovingAverage(2)
r=ma.compute([2,4,8,16,32,64,128,256,512])
print(r)
        