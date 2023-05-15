text="<<<<<<<<  Welcome to the ÇANAKKALE 1915 Game  >>>>>>>>"
print(text.upper())
print("\n--Choose you character--\n")
print("A = A78087 has 105 health and 10 strength")
print("B = B78087 has 60 health and 15 strength")
print("C = C78087 has 210 health and 1 strength")
a=input("")
if a=="A":
    print("Your character is A78087")
    print("Are you ready?")
    ask=input("Y/N\n")
    if ask=="Y":
        print("THE GAME WİLL START\n\n")
        print("""One day a young man was sitting on a bench. 
A man came to him and told him to get up and leave or something terrible would happen to him.
While the young man was thinking about what could happen, the man suddenly disappeared. 
Dark clouds suddenly surrounded him, and the youth noticed a glow ahead. 
He saw a young stone moving towards the light and wanted to touch the stone. 
The moment he touched it, he found himself on an incredible journey and arrived somewhere.\n
YEAR 1915!!\n""")
        print("""The young man came face to face with an enemy soldier on the Çanakkale front.
 He had a bag on his back and some energizing food in it.
 With a knife in his hand, the only condition for him to return is to lay down this enemy soldier and hang the Turkish flag there.""")
        i=1
        health1=105
        soldier1=120
        banana=5
        apple=2
        chicken=1
        while i==1:
          
            print("Enemy soldier health is: " , soldier1)
            print("Your health is:          " , health1)
            print("Number of banana:        ",banana)
            print("Number of apple:         ",apple)
            print("Number of chicken:       ",chicken,"\n")


            if health1>0 and soldier1>0:
                A=int(input(""" \n---------------------------\n
1: Eat banana for +10 health
2: Fight with enemy, every fight your health decrease 15 by 15 and you will reduce your enemy's health by 10
3: Eat apple for +15 health and you will reduce your enemy's health by 10
4: Eat chicken for +20 health\n"""))


                if A==1 and banana>0:
                    health1+=10
                    banana-=1
                elif A==2:
                    health1-=15
                    soldier1-=10
                elif A==3 and apple>0:
                    health1+=15
                    soldier1-=10
                    apple-=1
                elif A==4 and chicken>0:
                    health1+=20
                    chicken-=1
                else:
                    print("Enter a valid value!!!")
            elif soldier1==0:
                print("<<<<<<< You win you can back your home >>>>>>>")
                exit()
            else:
                print("<<<<<<< You death >>>>>>>")   
                exit()   


    elif ask=="N":
        print("Okay, you can play another time.")
    else:
        print("Enter a valid value!!!")
elif a=="B":
    print("Your character is B78087")
    print("Are you ready?")
    ask=input("Y/N\n")
    if ask=="Y":
        print("THE GAME WİLL START\n\n")
        print("""One day a young man was sitting on a bench. 
A man came to him and told him to get up and leave or something terrible would happen to him.
While the young man was thinking about what could happen, the man suddenly disappeared. 
Dark clouds suddenly surrounded him, and the youth noticed a glow ahead. 
He saw a young stone moving towards the light and wanted to touch the stone. 
The moment he touched it, he found himself on an incredible journey and arrived somewhere.\n
YEAR 1915!!\n""")
        print("""The young man came face to face with an enemy soldier on the Çanakkale front.
 He had a bag on his back and some energizing food in it.
 With a knife in his hand, the only condition for him to return is to lay down this enemy soldier and hang the Turkish flag there.""")
        z=1
        health2=60
        soldier2=120
        banana1=5
        apple1=2
        chicken1=1
        while z==1:
          
            print("Enemy soldier health is: " , soldier2)
            print("Your health is:          " , health2)
            print("Number of banana:        ",banana1)
            print("Number of apple:         ",apple1)
            print("Number of chicken:       ",chicken1,"\n")


            if health2>0 and soldier2>0:
                A=int(input(""" \n---------------------------\n
1: Eat banana for +10 health
2: Fight with enemy, every fight your health decrease 15 by 15 and you will reduce your enemy's health by 30
3: Eat apple for +15 health and you will reduce your enemy's health by 10
4: Eat chicken for +20 health\n"""))


                if A==1 and banana1>0:
                    health2+=10
                    banana1-=1
                elif A==2:
                    health2-=15
                    soldier2-=30
                elif A==3 and apple1>0:
                    health2+=15
                    soldier2-=10
                    apple1-=1
                elif A==4 and chicken1>0:
                    health2+=20
                    chicken1-=1
                else:
                    print("Enter a valid value!!!")
            elif soldier2==0:
                print("<<<<<<< You win you can back your home >>>>>>>")
                exit()
            else:
                print("<<<<<<< You death >>>>>>>")   
                exit()   


    elif ask=="N":
        print("Okay, you can play another time.")
    else:
        print("Enter a valid value!!!")
elif a=="C":
    print("Your character is C78087")
    print("Are you ready?")
    ask=input("Y/N\n")
    if ask=="Y":
        print("THE GAME WİLL START\n\n")
        print("""One day a young man was sitting on a bench. 
A man came to him and told him to get up and leave or something terrible would happen to him.
While the young man was thinking about what could happen, the man suddenly disappeared. 
Dark clouds suddenly surrounded him, and the youth noticed a glow ahead. 
He saw a young stone moving towards the light and wanted to touch the stone. 
The moment he touched it, he found himself on an incredible journey and arrived somewhere.\n
YEAR 1915!!\n""")
        print("""The young man came face to face with an enemy soldier on the Çanakkale front.
 He had a bag on his back and some energizing food in it.
 With a knife in his hand, the only condition for him to return is to lay down this enemy soldier and hang the Turkish flag there.""")
        x=1
        health3=210
        soldier3=120
        banana2=5
        apple2=2
        chicken2=1
        while x==1:
          
            print("Enemy soldier health is: " , soldier3)
            print("Your health is:          " , health3)
            print("Number of banana:        ",banana2)
            print("Number of apple:         ",apple2)
            print("Number of chicken:       ",chicken2,"\n")


            if health3>0 and soldier3>0:
                A=int(input(""" \n---------------------------\n
1: Eat banana for +10 health
2: Fight with enemy, every fight your health decrease 15 by 15 and you will reduce your enemy's health by 5
3: Eat apple for +15 health and you will reduce your enemy's health by 10
4: Eat chicken for +20 health\n"""))


                if A==1 and banana2>0:
                    health3+=10
                    banana2-=1
                elif A==2:
                    health3-=15
                    soldier3-=5
                elif A==3 and apple2>0:
                    health3+=15
                    soldier3-=10
                    apple2-=1
                elif A==4 and chicken2>0:
                    health3+=20
                    chicken2-=1
                else:
                    print("Enter a valid value!!!")
            elif soldier3==0:
                print("<<<<<<< You win you can back your home >>>>>>>")
                exit()
            else:
                print("<<<<<<< You death >>>>>>>")   
                exit()   


    elif ask=="N":
        print("Okay, you can play another time.")
    else:
        print("Enter a valid value!!!")
else:
    print("Enter a valid value!!!")
    exit()