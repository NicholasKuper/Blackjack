import math
import time
import random

Cards = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

stood = False
dealertotal = 0
dealeramount = 0
cardstotal = 0
cardamount = 0
FirstTime = True
Money = 100.0
Pokerface = 0
action = ""
Start = ""

def startup(action):
    global FirstTime
    global Money
    global Pokerface
    global Start
    global stood
    stood = False
    # Startup check #
    if Money == 0:
        print("You can't play!")
        time.sleep(2)
        return
    elif Money > 0:
        time.sleep(2)
        if FirstTime == True:
            print("Welcome to Blackjack!")
            time.sleep(1)
            print("You have $100 to start with.")
            time.sleep(1)
            print("There are two different gameplay mechanics: MONEY and POKERFACE.")
            time.sleep(3)
            print("The more POKERFACE, the more likely the dealer will fold. POKERFACE can be gained by winning MONEY rounds consecutively.")
            time.sleep(5)
            print("Are you ready?.")
            Start = input("yes or no: ")
            if Start == "yes":
                print("Let's begin!")
                FirstTime = False
                BlackJackStart()
            else:
                print("Goodbye!")
                time.sleep(2)
                return
        else:
            print("Welcome back!")
            time.sleep(1)
            print("You have $" + str(Money) + " to play with.")
            time.sleep(1)
            print("Are you ready?.")
            Start = input("yes or no: ")
            if Start == "yes":
                print("Let's begin!")
                BlackJackStart()
            else:
                print("Goodbye!")
                time.sleep(2)
                return

    # Gameplay #

def BlackJackAlgorithim(cardamount):
    card = random.choice(list(Cards.keys()))
    value = Cards[card]
    cardamount += value
    global cardstotal
    cardstotal += 1
    print("Card ", cardstotal, " is:", card)
    print("Your amount is:", cardamount)
    return card, cardamount

def DealerAlgorithim(dealeramount):
    dealer = random.choice(list(Cards.keys()))
    value = Cards[dealer]
    dealeramount += value
    global dealertotal
    dealertotal += 1
    print("Dealer Card #", dealertotal)
    return dealer, dealeramount

def BlackJackStart():
    global Money
    global Pokerface
    global cardamount
    global dealeramount
    global cardstotal
    global dealertotal
    global stood
    dealertotal = 0
    dealeramount = 0
    cardstotal = 0
    cardamount = 0
    print("What's your Ante?")
    Ante = float(input("Ante: "))
    print("What's your bet?")
    Bet = float(input("Bet: "))
    Money -= Ante + Bet
    print("Ante: $" + str(Ante))
    print("Bet: $" + str(Bet))
    card, cardamount = BlackJackAlgorithim(cardamount)
    time.sleep(1)
    dealer, dealeramount = DealerAlgorithim(dealeramount)
    time.sleep(1)
    card, cardamount = BlackJackAlgorithim(cardamount)
    time.sleep(1)
    dealer, dealeramount = DealerAlgorithim(dealeramount)
    time.sleep(1)
    if dealeramount == 21:
        print("Dealer Wins!")
        lose(Ante, Bet)
    elif cardamount == 21:
        print("You Win!")
        win(Ante, Bet)
    else:
        while True:
            if stood == False:
                hit = input("Do you want to hit? (yes/no) ")
                if hit == "yes":
                    card, cardamount= BlackJackAlgorithim(cardamount)
                    if cardamount > 21:
                        print("You Busted!")
                        lose(Ante, Bet)
                        break
                else:
                        stood = True
            else:
                if dealeramount > 15 and Pokerface > 2:
                    print("Dealer folds!")
                    win(Ante, Bet)
                    break
                elif dealeramount >= 21:
                    print("Dealer Busted!")
                    win(Ante, Bet)
                elif dealeramount == 21:
                    print("Dealer Wins!")
                    lose(Ante, Bet)
                    break
                else:
                    if dealeramount < 17:
                        dealer, dealeramount = DealerAlgorithim(dealeramount)
                    else:
                        if dealeramount < cardamount:
                            print("You Win!")
                            win(Ante, Bet)
                            break
                        elif dealeramount > cardamount:
                            print("You Loose!")
                            lose(Ante, Bet)
                            break
                        else:
                            dealer, dealeramount = DealerAlgorithim(dealeramount)


def lose(Ante, Bet):
    global dealertotal
    global dealeramount
    global cardstotal
    global cardamount
    dealertotal = 0
    dealeramount = 0
    cardstotal = 0
    cardamount = 0
    global Money
    global Pokerface
    print("You lose!")
    Pokerface = 0
    print("You have $" + str(Money) + " left.")
    print("You have " + str(Pokerface) + " POKERFACE.")
    action = input("Do you want to play again? (yes/no) ")
    if action == "yes":
        startup(action)
    else:
        print("Goodbye!")
        time.sleep(2)
        return

def win(Ante, Bet):
    global Money
    global Pokerface
    print("You win!")
    Money += (Ante + Bet)*3
    Pokerface += 1
    print("You have $" + str(Money) + " left.")
    print("You have " + str(Pokerface) + " POKERFACE.")
    action = input("Do you want to play again? (yes/no) ")
    if action == "yes":
        startup(action)
    else:
        print("Goodbye!")
        time.sleep(2)
        return

action = input("Do you want to start? (yes/no) ")
startup(action)