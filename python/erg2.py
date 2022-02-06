import random
steps=0
sum=0
caps=['s','m','l']
capsno2=['m','l']
for i in range(100):
    endgame=False
    mylist =['']*9
    sum+=steps
    while True:
        y=random.randint(0,8)# random position in mylist list
        if mylist[y]=='':
            mylist[y]=random.choice(caps)#random cap sto keno
            steps+=1 
        
        elif mylist[y]=='s':
            mylist[y]=random.choice(capsno2)# random cap megalytero toy small
            steps+=1 
        
        elif mylist[y]=='m':
            mylist[y]='l' #megalytero tou medium
            steps+=1
        print("               ")
        print("+----+---+---+")
        print("| "+mylist[0]+"  | "+mylist[1]+ " | "+mylist[2]+ " |") # print row1
        print("+----+---+---+")
        print("| "+mylist[3]+"  | "+mylist[4]+ " | "+mylist[5]+ " |") # print row2
        print("+----+---+---+")
        print("| "+mylist[6]+"  | "+mylist[7]+ " | "+mylist[8]+ " |") # print row3
        print("+----+---+---+")
        print("                ")

        #elegxos orizontia
        row1 = mylist[0] == mylist[1] == mylist[2] != ''
        row2 = mylist[3] == mylist[4] == mylist[5] != ''
        row3 = mylist[6] == mylist[7] == mylist[8] != ''
        if row1 or row2 or row3:
            endgame = True
        elif mylist[0] == 's' and mylist[1] == 'm' and mylist[2] == 'l':
            endgame = True
        elif mylist[3] == 's' and mylist[2] == 'm' and mylist[1] == 'l':
            endgame = True
        elif mylist[3] == 's' and mylist[4] == 'm' and mylist[5] == 'l':
            endgame = True
        elif mylist[5] == 's' and mylist[4] == 'm' and mylist[3] == 'l':
            endgame = True
        elif mylist[0] == 's' and mylist[1] == 'm' and mylist[2] == 'l':
            endgame = True
        elif mylist[3] == 's' and mylist[2] == 'm' and mylist[1] == 'l':
            endgame = True

        #elegxos katheta
        col1 = mylist[0] == mylist[3] == mylist[6] != ''
        col2 = mylist[1] == mylist[4] == mylist[7] != ''
        col3 = mylist[2] == mylist[5] == mylist[8] != ''
        if col1 or col2 or col3:
            endgame = True
        elif mylist[0] == 's' and mylist[3] == 'm' and mylist[6] == 'l':
            endgame = True
        elif mylist[6] == 's' and mylist[3] == 'm' and mylist[0] == 'l':
            endgame = True
        elif mylist[1] == 's' and mylist[4] == 'm' and mylist[7] == 'l':
            endgame = True
        elif mylist[7] == 's' and mylist[4] == 'm' and mylist[1] == 'l':
            endgame = True
        elif mylist[2] == 's' and mylist[5] == 'm' and mylist[8] == 'l':
            endgame = True
        elif mylist[8] == 's' and mylist[5] == 'm' and mylist[2] == 'l':
            endgame = True

        #elegxos diagwnia
        diag1 = mylist[0] == mylist[4] == mylist[8] != ''
        diag2 = mylist[6] == mylist[4] == mylist[2] != ''
        if diag1 or diag2:
            endgame = True
        elif mylist[0] == 's' and mylist[4] == 'm' and mylist[8] == 'l':
            endgame = True
        elif mylist[8] == 's' and mylist[4] == 'm' and mylist[0] == 'l':
            endgame = True
        elif mylist[2] == 's' and mylist[4] == 'm' and mylist[6] == 'l':
            endgame = True
        elif mylist[6] == 's' and mylist[4] == 'm' and mylist[2] == 'l':
            endgame = True                  

        if endgame==True  :
            break #the loop 

mo=sum/100 #mesos oros
print("Mesos oros bhmatwn: " , mo)  
