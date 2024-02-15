









myf=open('data.csv')
list=[]
for line in myf:
    line=line.split(',')
    line[-1]=line[-1].strip()
    list.append(line)

    #line=line.split(',')
    #if line[0]!='date':
     #   line[-1]=line[-1].strip()
      #  list.append(line)
#print(list)
lista=[]
for el in list:
    if el[0]!='date':
        el[0]=el[0].split('-')
        lista.append(el[0])
print(lista)
f=int(lista[3][0])+int(lista[3][1])
print(f)
if int(list[3][0][0])==4:
    print(list[3][0])
    print('si')

""""
listalista=[]
p=0
for i in list:
    p=p+1
    listat=[]
    listat.append(lista[p-1][0])
    listat.append(lista[p-1][1])
    listat.append(list[p-1][1])
    listalista.append(listat)
    
print(lista)   
#    listlist=[]
 #   file=open(self.name,'r')
  #  for line in file:
  #      el=line.split(',')
   #     el[-1]=el[-1].strip()"""
