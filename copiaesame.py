class ExamException(Exception):
    pass
    
class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
    def get_data(self):
       # La serie temporale nel file CSV è da considerare sempre ordinata, se per caso ci dovesse essere un timestamp fuori ordine va alzata un'eccezione (dentro la funzione get_data()) senza cercare di riordinare la serie. Stesso discorso se c’è un timestamp duplicato: si alza un'eccezione.
        try:
            myfile=open(self.name,'r')
            for line in myfile:
                myfile.readline()
            myfile.close
        except Exception as e:
            raise ExamException('Errore in apertura o lettura') from e
        #Il file CSV può contenere letteralmente di tutto. Da linee incomplete a pezzi di testo che non c’entrano niente, e ogni errore salvo quello di un timestamp fuori ordine o duplicato va ignorato (ovvero, ignoro la riga contenente l’errore e vado a quella dopo). 
        listlist=[]
        file=open(self.name,'r')
        for line in file:
            el=line.split(',')
            el[-1]=el[-1].strip()
            if el[0]!='date':
                if type(el[1])!=int:
                    try:
                        int(el[1])
                    except:
                        print('Valore non numerico in data {}'.format(el[0]))
                        continue 
                if int(el[1])<=0:
                    print('Valore nullo in data {}'.format(el[0]))
                
                    
                listlist.append(el)
        if listlist==[]:
            raise ExamException('Lista di valori vuota')
        #cont=0
        #for el in listlist:
         #   cont=cont+1
          #  for lol in listlist[cont:]:
           #     if lol[0]==el[0]:
            #        raise ExamException('timestamp doppio: {}'.format(lol[0]))
        return listlist





def compute_increments(time_series, first_year, last_year):
    if type(first_year)!=str:
        raise ExamException('Inizio non stringa, invalido')
    try:
        first_year=int(first_year)
    except Exception as e:
        raise ExamException('Inizio non numerabile') from e
    #da vedere se è nel csv
    if type(last_year)!=str:
        raise ExamException('Fine non stringa, invalido')
    try:
        last_year=int(last_year)
    except Exception as e:
        raise ExamException('Fine non numerabile') from e 
    #da vedere se è nel csv
    if int(first_year)==int(last_year):
        raise ExamException('Intervallo troppo piccolo')
     #se l’intervallo considerato è 1949, 1950, 1951 e per l’anno 1950 non abbiamo misurazioni, l’incremento nel numero di passeggeri per anni verrà calcolato tra l’anno 1951 e l’anno 1949. Se invece l’intervallo considerato è di soli due anni e per uno dei due anni non abbiamo misurazioni, l’output sarà una lista vuota.
    first_year=str(first_year)
    last_year=str(last_year)
    m=int(last_year)-int(first_year)+1    #ampiezza intervallo da anno ad anno
    lista_medie=[]

    
    c=0
    p=0
    med=0
    for i in range(m):
        while first_year in time_series[p][0]:
            if type(time_series[p+12*i][1])!=int:
                try:
                    time_series[p+12*i][1]=int(time_series[p+12*i][1])
                except:
                    print('Valore non numerico in data {}'.format(time_series[p+12*i][0]))
                    c=c-1
                    continue 
            med=med+int(time_series[p+12*i][1])
            if med==med-int(time_series[p+12*i][1]):
                print('cè un valore nullo')
                c=c-1
            p=p+1
            c=c+1
        lista_medie.append(med/c)
        med=0
        p=0
        c=0
    print(lista_medie)
    print('\n')
#da vedere nel caso di un anno vuoto
    
    c=0
    diff=0
    lista_scarti=[]
    while c<(m-1):
        a=lista_medie[c]
        b=lista_medie[c+1]
        diff=b-a
        lista_scarti.append(diff)
        c=c+1
    print(lista_scarti)
    print('\n')

    
    z=1
    lista_anni=[]
    while z<m:
        anni1=str(int(first_year)+z-1)
        anni2=str(int(first_year)+z)
        lista_anni.append(anni1+"-"+anni2)
        z=z+1
    print(lista_anni)
    print('\n')

    
    dizionario={}
    for i in range(m-1):
        dizionario[lista_anni[i]]=lista_scarti[i]
    return dizionario
  
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()
#print(time_series)
print(compute_increments(time_series, '1949','1952'))