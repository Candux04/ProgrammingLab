#scrivi una funz sum_csv(file_name) che sommi i valori delle vendite

def sum_csv(file_name):
    valori=[]               #lista di valori, all'inizio vuota
    my_file=open(file_name) #apro un file, assocerò poi shampcsv
    for line in my_file:
        print(line)
        elements=line.split(',') #stacca le date dai valori  
        if elements[0] !='Date': #se sono nella prima parte(Date,Sales)
            valore=float(elements[1]) #converto sales da str a float 
            print(valore,'\n')
            valori.append(valore) #aggiungo sales alla lista di valori
    if valori==[]: #se la lista è vuota, non ritorno nulla
        return None
    return sum(valori)

    
#Per eseguire: vvv
#somma=sum_csv('shampoo_sales2.csv') #chiamo funz con il file shampcsv
#print('somma =',somma)