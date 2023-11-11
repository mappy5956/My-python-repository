print("Welcome to Treasue Island")
print("Do you want to go left or right:\ntype 'left' or 'right'")
Direction=input()
Direction=Direction.lower()
if Direction=='right':
    print('You have entered in a Dark Cave')
    print('In the Dark cave you have three options \n1.crawl through a small passage \n2.climb out of the cave as it has a hugh opening in \n3.Enter a secret door\n please type either crawl,climb or door')
    rightchoice=input().lower()
    if rightchoice=='crawl':
        print('You are bitten by multiple animal in  the tunnel and died,\nGame over!')
    elif rightchoice=='climb':
        print('Congratulation you have found 10000 gold coins chest at the top top of the tunnel,You Win')
    elif rightchoice=='door':
        print('A axe comes by swinging and decapitates you and you died,\nGame over!')
if Direction=='left':
    print("You have entered a Jungle and found a lion Do you want to fight the lion or climb the tree -type either 'climb' or 'fight':")
    leftchoice=input().lower()
    if leftchoice=='fight':
        print('The lion injures you and you died,\nGame over!')
    elif leftchoice=='climb':
        print('The lion waits for a while and then walks away,Congratulations you are still alive')
        print("You come across a river \n1)Do you swim or \n2)wait for the boat \ntype either 'swim' or 'wait'")
        leftchoice1=input().lower()
        if leftchoice1=='swim':
            print("piranha in the river eats you and you died,\nGame over!")
        elif leftchoice1=='wait':
            print("You have waited for a boat and crossed the river,\nyou have found three trees with three cross underneath them ")
            print("You have to choose one cross to dig out of three,which cross do you choose to dig?\n1)red\n2)blue\n3)green\n type either 'red'or 'green'or'blue'")
            crosschoice=input().lower()
            if crosschoice=='red':
                print("you hit a landmine and died,\nGame over!")
            elif crosschoice=='blue':
                print("you a found a chest with 10,000 gold you win")
            elif crosschoice=='green':
                print("you hit a switch and venomous gas enter the hole and you died!\nGame over!")
