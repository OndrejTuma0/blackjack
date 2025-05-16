import random

deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]

def updateTotal(list):
    total = 0
    for x in list:
        if x.isnumeric() == True:
            total += int(x)
        elif x.isnumeric() == False:
            if x == "A":
                if total + 11 > 21:
                    total += 1
                else:  
                    total += 11
            else:
                total += 10
    return total

def results():
    print("-------------------")
    print(f"Dealer's deck: {dealer} | Total: {dealerTotal}")
    print(f"Your deck: {you} | Total: {youTotal}")
    if dealerTotal > 21:
        print("You win!")
    elif dealerTotal > youTotal:
        print("You lose!")
    elif dealerTotal < youTotal:
        print("You win!")
    elif dealerTotal == youTotal:
        print("Push!")

dealer = random.choices(deck, k=2)
deck.remove(dealer[0])
deck.remove(dealer[1])

you = random.choices(deck, k=2)
deck.remove(you[0])
deck.remove(you[1])

dealerTotal = updateTotal(dealer)
youTotal = updateTotal(you)

while True:
    print("-------------------")
    print(f"Dealer's deck: {dealer[0]}, ?")
    print(f"Your deck: {you} | Total: {youTotal}")
    choice = input("Hit or stand?: ")
    if choice == "hit":
        pull = random.choice(deck)
        you.append(pull)
        deck.remove(pull)
        youTotal = updateTotal(you)
        if youTotal > 21:
            print("-------------------")
            print(f"Your deck: {you} | Total: {youTotal}")
            print(f"Bust!")
            print("-------------------")
            playAgain = input("Play again? (y/n): ")
            if playAgain == "y":
                deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
                dealer = random.choices(deck, k=2)
                deck.remove(dealer[0])
                deck.remove(dealer[1])
                you = random.choices(deck, k=2)
                deck.remove(you[0])
                deck.remove(you[1])
                dealerTotal = updateTotal(dealer)
                youTotal = updateTotal(you)
                pass
            elif playAgain == "n":
                break
    elif choice == "stand":
        if "A" in dealer and dealerTotal == 17:
            pull = random.choice(deck)
            dealer.append(pull)
            deck.remove(pull)
            dealerTotal = updateTotal(dealer)
            results()
            break
        while dealerTotal <= 16:
            pull = random.choice(deck)
            dealer.append(pull)
            deck.remove(pull)
            dealerTotal = updateTotal(dealer)
        results()
        print("-------------------")
        playAgain = input("Play again? (y/n): ")
        if playAgain == "y":
            deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
            dealer = random.choices(deck, k=2)
            deck.remove(dealer[0])
            deck.remove(dealer[1])
            you = random.choices(deck, k=2)
            deck.remove(you[0])
            deck.remove(you[1])
            dealerTotal = updateTotal(dealer)
            youTotal = updateTotal(you)
            pass
        elif playAgain == "n":
            break