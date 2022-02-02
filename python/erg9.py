f = open('tale.txt')
txt = str(f.read())
newtxt = ''.join('{0:07b}'.format(ord(c), 'b') for c in txt)#metatroph se 7 bit binary
max=0#max akolouthia 0
max2=0#max akolouthia 1
continuous0=0#synexomena 0
continuous1=0#synexomena 1
newlength=len(newtxt)
for i in range(newlength):
    if newtxt[i]=='0':
        continuous0+=1
    else:
        if max<continuous0:
            max=continuous0
        continuous0=0

for i in range (newlength):
    if newtxt[i]=='1':
        continuous1+=1
    else :
        if max2<continuous1:
            max2=continuous1
        continuous1=0
print("Megalyterh akolouthia 0: ", max)
print("Megalyterh akolouthia 1: ", max2)