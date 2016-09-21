import random, os, datetime
from time import strftime

class Thelist(object):

    def pickert(self):
        # These are the time and day of right now
        nownew = datetime.datetime.now().date()
        # Opens the file so it can be read 
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Randomly picks an item from the list
        self.randomly = random.choice(newlist)
        # Removes the item you randomly picked earlyer
        newlist.remove(self.randomly)
        # Writing the time and day to file
        d = open ('tshirt_date.txt', 'w')
        d.write(strftime("%A "))
        d.write(str(nownew))
        d.write(" - Number %s was picked" % self.randomly)
        d.close()
        # Writting the log for each time you pick a t-shirt and what number is picked
        d = open ('tshirt_log.txt', 'a')
        d.write(strftime("%A "))
        d.write(str(nownew))
        d.write(" - Number %s was picked" % self.randomly)
        d.write("\n")
        d.close()
        # Writes the list to file and closes the file to save it
        f = open ('tshirt.txt', 'w')
        f.write(str(newlist))
        f.close()

    def addlist(self):
        # Opens the file so it can be read
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Shows you what you have in your list so you know what to add to it
        print "Here is the list so far %s" % sorted(newlist)
        print "There are %s t-shirts in the list" % len(newlist)
        # Asks you what you want to add to the list
        addit = raw_input("Enter number you want to add to the list > or exit to exit > ")
        while addit != 'exit':
            # Adds the raw_input to the list
            newlist.append(addit)
            print "%s has been added to the list" % addit
            print "Here is what's in the list %s" % sorted(newlist)
            print "There are %s t-shirts in the list" % len(newlist)
            # Opens the files to be writen
            f = open ('tshirt.txt', 'w')
            # Writes the list to the files
            f.write(str(newlist))
            # Closes the file
            f.close()
            addit = raw_input("Enter number you want to add to the list > or exit to exit > ")
            if addit == 'exit':
                exit()
        
    def firsttime(self):
        # Empty list
        newlist = []
        addit = raw_input("Enter number you want to add to the list > ")
        # Adds the raw_input to the list
        newlist.append(addit)
        print "%s has been added to the list" % addit
        print "Here is what's in the list %s" % sorted(newlist)
        # Opens the files to be writen
        f = open ('tshirt.txt', 'w')
        # Writes the list to the files
        f.write(str(newlist))
        # Closes the file
        f.close()
        exit()
        
    def removelist(self):
        # Opens the file so it can be read
        a = open ('tshirt.txt', 'r')
        # Loads the list to be used as a list using the eval command
        newlist = eval(a.read())
        # Shows you what you have in your list so you know what to add to it
        print "Here is the list so far %s" % sorted(newlist)
        # Asks you what you want to add to the list
        removeit = raw_input("Enter ether a number of a t-shirt or a description > ")
        while removeit != 'exit':
            # Adds the raw_input to the list
            newlist.remove(removeit)
            print "%s Has been removed from the list" % removeit
            print "There are %s t-shirts in the list" % len(newlist)
            print "Here is what's in the list %s" % sorted(newlist)
            # Opens the files to be writen
            f = open ('tshirt.txt', 'w')
            # Writes the list to the files
            f.write(str(newlist))
            # Closes the file
            f.close()
            removeit = raw_input("Enter ether a number of a t-shirt or a description or exit to exit > ")
            if removeit == 'exit':
                exit()
                
    def log_list(self):
        log = open ('tshirt_log.txt', 'r')
        read_log = log.read()
        print read_log
        
if __name__ == '__main__':
    start = Thelist()
print '''
ooooooooooo       oooooooo8 oooo        o88                o8   
88  888  88      888         888ooooo   oooo  oo oooooo  o888oo 
    888 ooooooooo 888oooooo  888   888   888   888    888 888   
    888                  888 888   888   888   888        888   
   o888o         o88oooo888 o888o o888o o888o o888o        888o 
                                                                
oooooooooo  o88             oooo                                
 888    888 oooo   ooooooo   888  ooooo ooooooooo8 oo oooooo    
 888oooo88   888 888     888 888o888   888oooooo8   888    888  
 888         888 888         8888 88o  888          888         
o888o       o888o  88ooo888 o888o o888o  88oooo888 o888o

ver 0.1.0 beta
The day and time picker with logs edition    
 '''
# This looks to see if there is anything in the tshirt.txt file by reading the bytes
lenthlist = os.stat("tshirt.txt").st_size
# If there is nothing in the file it sends you to add items to your list
if lenthlist <=0:
    print "There is nothing in your list"
    start.firsttime()
else:
    # Opens the tshirt_date file to show you when you last picked your last tshirt
    d = open ('tshirt_date.txt', 'r')
    times = d.read()
    # Opens the tshirt file to show you the list
    a = open ('tshirt.txt', 'r')
    newlist = eval(a.read())
    print "T-shirt list %s\n" % sorted(newlist)
    print "Last t-shirt was picked %r \n" % times
    asking = raw_input("""Enter the number of what you want to do:\n'1'> Pick\n'2'> Add\n'3'> Remove\n'4'> View log\n'5'> Exit\n> """)
    if asking == "1":
        start.pickert()
        print "%s Has been randomly pick for you to wear" % start.randomly    
    elif asking == "2":
        start.addlist()
    elif asking == "3":
        start.removelist()
    elif asking == "4":
        start.log_list()
    elif asking == "5":
        exit()
    else:
        print "Something went wrong"
