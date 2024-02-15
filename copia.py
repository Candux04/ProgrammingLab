class ExamException(Exception):
    pass
    
class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
    def get_data(self):
        try:
            myfile=open(self.name,'r')
            for line in myfile:
                myfile.readline()
            myfile.close
        except Exception as e:
            raise ExamException('Errore in apertura o lettura') from e
        listlist=[]
        file=open(self.name,'r')
        for line in file:
            el=line.split(',')
            el[-1]=el[-1].strip()
            if el[0]!='date': 
                if len(el)!=2:
                    continue
                if type(el[1])!=int:
                    try:
                        el[1]=int(el[1])
                    except:
                        #print('Valore non numerico in data {}'.format(el[0]))
                        continue 
                
                try:
                    pro=el[0].split('-')
                    an=int(pro[0])
                    me=int(pro[1])
                except:
                    continue
               # if int(el[1])<=0:
                #    print('Valore nullo in data {}'.format(el[0]))
                
                    
                listlist.append(el)
        if listlist==[]:
            raise ExamException('Lista di valori vuota')
        for li in range(len(listlist)):
            for st in listlist[(li+1):]:
                if st[0]==listlist[li][0]:
                    raise ExamException('Timestamp {} duplicato'.format(st[0]))
                    
        listam=[]
        for el in listlist:
            el[0]=el[0].split('-')
            listam.append(el[0])
        listamm=[]
        for c in range(len(listam)-1):
            nnn=(int(listam[c][0])-1949)*100
            nnn=nnn+int(listam[c][1])
            listamm.append(nnn)
        for p in range(len(listamm[0:-1])):
            if int(listamm[p])>int(listamm[p+1]):
                raise ExamException('Timestamp fuori ordine')
        return listlist





def compute_increments(time_series, first_year, last_year):
    if type(first_year)!=str:
        raise ExamException('Inizio non stringa, invalido')
    try:
        first_year=int(first_year)
    except Exception as e:
        raise ExamException('Inizio non numerabile') from e
    v=False
    for el in time_series:
        if str(first_year) in el[0]:
            v=True
    if v is False:
        raise ExamException('Anno iniziale non presente')
    if type(last_year)!=str:
        raise ExamException('Fine non stringa, invalido')
    try:
        last_year=int(last_year)
    except Exception as e:
        raise ExamException('Fine non numerabile') from e 
    v=False
    for el in time_series:
        if str(last_year) in el[0]:
            v=True
    if v is False:
        raise ExamException('Anno finale non presente')
    if int(first_year)==int(last_year):
        raise ExamException('Intervallo troppo piccolo')
    if int(first_year)>int(last_year):
        raise ExamException('Intervallo non valido')

    
    first_year=str(first_year)
    last_year=str(last_year)
    m=int(last_year)-int(first_year)+1    #ampiezza intervallo da anno ad anno
    f=int(first_year)-1949                #quanti anni salto dall'inizio
    lista_medie=[]

    listap=[]
    c=0
    p=0
    med=0
    for i in range(m):
        while first_year in time_series[p+12*f][0]:
            med=med+time_series[p+12*i+12*f][1] 
            if med==med-time_series[p+12*i+12*f][1]:
                #print('cè un valore nullo')
                c=c-1
            if type(time_series[p+12*i][1])!=int:
                try:
                    time_series[p+12*i][1]=int(time_series[p+12*i+12*f][1])
                except:
                    el=time_series[p+12*i+12*f]
                    #print('Valore non numerico in data {}'.format(el[0]))
                    c=c-1
                    continue 
            p=p+1
            c=c+1
        listap.append(c)
        if c==0:
            c=1
        lista_medie.append(med/c)
        med=0
        p=0
        c=0
    print(lista_medie)
    #print(listap)

    
    if m==2 and lista_medie[0]==0:
       # print('Anno {} vuoto'.format(first_year))
        lista_medie=[]
        return lista_medie
    if m==2 and lista_medie[1]==0:
       # print('Anno {} vuoto'.format(last_year))
        lista_medie=[]
        return lista_medie
    for i in range(len(lista_medie)):
        if listap[i]==0:
            fff=str(int(first_year)+i)
           # print('Anno {} diocc vuoto'.format(fff))
            
    amp=m
    lista_scarti=[]
    lista_anni=[]
    t=1
    while t<amp:
        a=lista_medie[t-1]
        b=lista_medie[t]
        if lista_medie[t]==0:
            t=t+1
            b=lista_medie[t]
        diff=b-a
        lista_scarti.append(diff)
        anni1=str(int(first_year)+t-1)
        if lista_medie[t-1]==0:
            anni1=str(int(anni1)-1)
        anni2=str(int(first_year)+t)
        lista_anni.append(anni1+"-"+anni2)
        t=t+1
    print(lista_scarti) 
    print(lista_anni)


    dizionario={}
    for i in range(len(lista_scarti)):
        dizionario[lista_anni[i]]=lista_scarti[i]
    return dizionario


#SOLO PER ESEGUIRE VVVVV
time_series_file=CSVTimeSeriesFile(name='data2.csv')
time_series=time_series_file.get_data()
#print(time_series)
print(compute_increments(time_series, '1949','1952'))