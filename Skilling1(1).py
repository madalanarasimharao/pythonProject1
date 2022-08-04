import random
class ticketPrinting:
    def printTicket(self,str,gender,pick,destination):
        print("**PASSENGER TICKET**")
        print("PNR NUMBER",random.randint(999999,100000000))
        print("name:",str)
        print("Gender:",gender)
        print("from",pick,"to",destination)


class manager(ticketPrinting):
    name=input("enter passenger name: ")
    gender=input("enter passenger gender: ")
    pick=input("enter starting point: ")
    destination=input("enter destination: ")
    obj=ticketPrinting()
    obj.printTicket(name,gender,pick,destination)



