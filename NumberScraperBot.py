from googlesearch import search
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style

colorama.init()

#gotta initialize values here, get the values from a txt
startthing=0 #will change later
numberlist = []#will change later

coolcybervisionlogo = """
                         `.-://++++++//:-.`
                    .:/+++++++oooooo+++++++/:.
                 .:+++++syyhddddddddddhyys+++++:.
               ./+++oyhddddddddddddddddddddhyo+++/-
             ./+++shddddddddddddddddddddddddddhs+++/.
            :+++ohdddddddhhhddddddddddddddddddddhs+++:
          `/+++ydddddyso++++++oshdddddddddddddddddy+++/`
          /+++hddddyo+++syyyysoodddddddddddddddddddho++/
         :+++hddddy+++smmmmmmmmmmmmdddddddddddddddddh+++:
        `+++ydddddo++ommmmmmmmmmmmmmdddddddddddddddddy+++.
        :+++dddddd+++smmmmmmmmmmmmmmmmdddddddddddddddd+++:
        /++odddddds+++hmmmmmmmmmmy++ommddddh+++ddddddds+++
        +++sddddddds+++oyhddhyssdd+++ymmmddo++smmddddds+++
        /++oddddddddhyo++++++++ohmy+++dmmmy+++dmmmmddds+++
        :+++ddddddddddmmdhhhhdmmmmmo++smmd+++ymmmmmmdd+++:
        `+++yddddddddddmmmmmmmmmmmmd+++hmo++ommmmmmmmy+++.
         :+++hdddddddddddmmmmmmmmmmmy+++s+++dmmmmmmmd+++:
          /+++hdddddddddddmmmmmmmmmmmo+++++ymmmmmmmdo++/`
          `/+++ydddddddddddmmmmmmmmmmh++++ommmmmmmh+++/`
            :+++shdddddddddddmmmmmmmmmhyyhdmmmmmds+++:
             ./+++shddddddddddmmmmmmmmmmmmmmmmdy+++/.
               -/+++oyhddddddddmmmmmmmmmmmmdyo+++/-
                 .:++++osyyhdddddmmmmmdhyso++++:.
                    .:/+++++++ooooooo++++++/:.
                        .--://++++++//::-.`      """
print(Fore.GREEN + coolcybervisionlogo + "\n\nCyberSearcher has started up!")

def menu(): #menu
    while True:
        text = "Enter a number from 1-4 to choose an option\n1. Look for scammer numbers\n2. List all found numbers\n3. Clear all numbers (DISCLAIMER: This will wipe all numbers stored and you cannot get them back)\n4. Exit the program."
        print(Style.RESET_ALL + "\n" + text + "\n")
        try:
            number = int(input())

            if number < 1 or number > 4:
                print("\nYou need to enter an integer from 1-3.")

            if number == 1:
                amountofnumbers = int(input("How many numbers do you want to receive? "))
                print("\nLooking for numbers...")
                for j in search("tech support toll free number", num=amountofnumbers,start=startthing,stop=1,pause=2): #you may lower the pause number to make it run faster, but google might block your ip.
                    #you may also change what you are searching, the default is "tech support toll free number"
                    print(j)
                    #will append numbers to the list and then put in txt file

            if number == 2:
                print(numberlist)#I have yet to do this, prob gonna store all numbers on a txt

            if number == 3:
                yesorno = input("\nAre you sure? Enter \"yes\" to proceed\n")
                if yesorno == "yes":
                    print("Clearing numbers")
                    #add code to clear numbers
                    print("Cleared all numbers!")
                else:
                    print("\nNumbers will not be deleted")

            if number == 4:
                exit()

        except ValueError:
            print("\nYou didn't enter an integer and caused an error, don't do it again lol.")
            continue

menu()
#todo: add the numbersearcher part and you're done