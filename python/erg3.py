import string
allowed_chars=string.ascii_letters +" "
with open ("tale.txt") as f:
    txt=f.read()
newtxt = ''.join(c for c in txt if c in allowed_chars)
#split list
arr=newtxt.split(" ")
#without spaces
arr = list(filter(('').__ne__, arr))#remove ''
newtxt=arr
length=len(newtxt)
#remove pairs of words with sum 20
for i in range (0,length-1):
    x=len(newtxt[i])
    if x<20:
        y=len(newtxt[i+1])
        if y+x==20:
            newtxt[i]=''
            newtxt[i+1]=''

newtxt = list(filter(('').__ne__, newtxt))#remove ''
#new list length 
newlength=len(newtxt)
max=-1
pl=[] #new list for statics

for i in range (newlength):
    if max<len(newtxt[i]):
        max=len(newtxt[i])

for i in range (max):
    pl.append(0) 

for i in range(newlength):
    pl[len(newtxt[i])-1]+=1

for i in range(len(pl)):
    print ("Yparxoun ",pl[i]," lejeis me ",i+1," grammata")    