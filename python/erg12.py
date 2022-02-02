import requests
import json
import string
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
last=data["round"]
list1=[]
for i in range (last,last-100,-1):
    r = requests.get('https://drand.cloudflare.com/public/%d'%(i), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    list1.append(data["randomness"])

length=len(list1)
for i in range (length):
    list1[i]=str(bin(int(list1[i],base=16)))#convert in binary
    list1[i]=list1[i][2:]#remove 0b

connect=''.join(list1)
max=0#max akolouthia 0
max2=0#max akolouthia 1
continuous0=0#synexomena 0
continuous1=0#synexomena 1
newlength=len(connect)
for i in range(newlength):
    if connect[i]=='0':
        continuous0+=1
    else:
        if max<continuous0:
            max=continuous0
        continuous0=0

for i in range (newlength):
    if connect[i]=='1':
        continuous1+=1
    else :
        if max2<continuous1:
            max2=continuous1
        continuous1=0
print("Megalyterh akolouthia 0: ", max)
print("Megalyterh akolouthia 1: ", max2)