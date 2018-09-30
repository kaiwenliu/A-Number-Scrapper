from google import google
import urllib.request
import colorama
from colorama import Fore, Style
import re

colorama.init()
listoflegitsites = ["https://support.microsoft.com",""]#todo: implement this later
searchphrase = "toll free tech support intitle:800" #change this if you would like (not recommended)
pausetime = 2 #you may lower the pause number to make it run faster, but google might block your ip.
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
        #gotta initialize values here, get the values from a txt
        with open('Numbers.txt') as f:
            nolinelist = [line.rstrip('\n') for line in f]
        numberlist = "".join(nolinelist).split("|")
        if numberlist[0] == "":
            numberlist = []
        startthing = len(numberlist)#where to start
        text = "There are currently " + str(len(numberlist)) + " numbers scraped. " + "\n\nEnter a number from 1-4 to choose an option\n1. Look for scammer numbers\n2. List all found numbers\n3. Clear all numbers (DISCLAIMER: This will wipe all numbers stored and you cannot get them back)\n4. Exit the program."
        print(Style.RESET_ALL + "\n" + text + "\n")
        try:
            number = int(input())

            if number < 1 or number > 4:
                print("\nYou need to enter an integer from 1-3.")

            if number == 1:
                amountofnumbers = int(input("\nHow many numbers do you want to receive? "))
                amountofiterations = 0
                print("\nLooking for numbers...\n")
                search_results = google.search(searchphrase,amountofnumbers)
                while True:
                    if amountofnumbers == amountofiterations:
                        break
                    #you may also change what you are searching, the default is "tech support toll free number"
                    with urllib.request.urlopen(search_results[amountofiterations].link) as url:
                        sitetext = url.read().decode("utf-8")
                    listofnumbersfromj = re.findall(r"(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})", sitetext)
                    listofnumbersfromj = list(set(listofnumbersfromj))
                    if len(listofnumbersfromj) == 0:
                        continue #if there are no numbers then continue
                    else:
                        print("====================================")
                        print(search_results[amountofiterations].link)
                        print("====================================")
                        writeNumbers = open("Numbers.txt","w")
                        for h in range(0,len(listofnumbersfromj)):
                            print(listofnumbersfromj[h])
                            if h == len(listofnumbersfromj) - 1:
                                writeNumbers.write(listofnumbersfromj[h])
                            else:
                                writeNumbers.write(listofnumbersfromj[h] + "|")
                        amountofiterations += 1
                        #will append numbers to the list and then put in txt file
            if number == 2:
                for k in range(0,len(numberlist)):#I have yet to do this, prob gonna store all numbers on a txt
                    print(numberlist[k])
            if number == 3:
                yesorno = input("\nAre you sure? Enter \"yes\" to proceed:\n")
                if yesorno == "yes":
                    print("\nClearing numbers")
                    open('Numbers.txt', 'w').close()
                    print("\nCleared all numbers!")
                else:
                    print("\n\nNumbers will not be deleted")

            if number == 4:
                exit()

        except Exception as e:
            print(str(e))
            continue

menu()
