l=[]
bal=[]
log=[]
n_players=int(input("Enter the number of players: "))
def set_init_cash(cash):
    for i in range(n_players):
        bal.append(cash)
    bal.append(99999999999999999) #basically unli cash for the bank
init_cash_per_player = float(input("Enter the initial cash per player you wanna start with (in millions): "))
set_init_cash(init_cash_per_player)
def pay(i,amt):
    if bal[i]-amt<0:
        print("You will go bankrupt cant do this plz mortgage some of the properties or quit")
    else:
        bal[i]-=amt
def get_log():
    print(log)
def gain(i,amt):
    bal[i]+=amt
def transfer(i,j,amt):
    pay(i,amt)
    gain(j,amt)
def get_player_id(string):
    flag=0
    for i in range(len(l)):
        if l[i]==string or l[i][0]==string:
            flag=1
            return i
    if flag==0 :
        print("Check the name you have entered so we have assumed the money is being transferred to the bank")
        return n_players #basically the bank id
for i in range(n_players):
    print("Enter the name of player " ,i+1,": ",end="")
    l.append(input())
l.append("bank")
storageid1=0
storageid2=0
storageamt=0
def redo_the_last_transaction():
    transfer(storageid2,storageid1,amount)
    log.pop()
while(True):
    try:
        for i in range(n_players):
            print(l[i].upper(),": net balance = ",bal[i]," Million")
        """here is how to write:
                 utkarsh pay bank 1000M """
        entered = input().split()
        log.append(entered)
        if entered[0]=='go':
            id0 = get_player_id(entered[1])
            gain(id0,2)
            continue
        if entered[0]== 'redo':
            redo_the_last_transaction()
            continue
        if entered[0]=='log':
            get_log()
            continue
        if entered[0]=='stop':
            maxbal=0
            maxid=n_players
            for z in range(n_players):
                if maxbal<bal[z]:
                    maxbal = bal[z]
                    maxid=z
            print("The winner is: ",l[maxid].upper()," with an amount of: ",bal[maxid], "Million")
            break
        id1 = get_player_id(entered[0])
        id2 = get_player_id(entered[2])
        amount=0
        if entered[3][-1].upper()== "K":
            amount=float(entered[3][0:-1])/1000
        else:
            amount=float(entered[3][0:-1])
        transfer(id1,id2,amount)
        storageamt=amount
        storageid1=id1
        storageid2=id2
    except:
        print("You can redo if some transaction has occurred: ")
