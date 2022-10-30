print("WELCOME TO KBC")
print("ALL THE BEST FOR YOUR GAME")
question=["what is your name?","what is your age","where are you from?","capital of india?"]
options=[["anshi","aashi","anshita","aansita"],["20","14","19","18"],["mumbai","udaipur","delhi","punjab"],["delhi","rajasthan","punjab","bihar"]]
lifeline=[["anshita","anshi"],["20","19"],["udaipur","mumbai"],["bihar,delhi"]]
ans=[3,1,2,1]
ans1=[1,1,1,2]
i=0
count=0
while i<len(question):
    print("Q.",i+1,question[i])
    j=0
    while j<len(options):
        print(j+1,options[i][j])
        j+=1
    user=int(input("enter the option : "))
    if user==ans[i]:
        print("WOW! CONGRATULATIONS")
    elif user==5050:
        if count==0:
            k=0
            while k<len(lifeline):
                print(k+1,lifeline[i][k])
                k+=1
            count+=1
            user1=int(input("enter : "))
            if user1==ans1[i]:
                print("correct")
            else:
                print("wrong")
                break
        else:
            print("you are already used")
            num=int(input("enter any number"))
            if num==ans[i]:
                print("correct")
            else:
                print("oops! sorry")
    else:
        print("sorry...better luck for next time")
        break
    i+=1
