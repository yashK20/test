text=list(input("enter text: "))
k=list(input("enter key: "))
key=[]
for i in k:
    if i not in key:
        key.append(i)
while ' ' in text:
    text.remove(' ')
ip=k+text
ips=[]
key.sort()
l=[]
for i in range(0,len(key)):
    for j in range(0,len(key)):
        if(key[i]==ip[j]):
            ips=ips+text[j::len(key)]
print(ips)
            
        

        
