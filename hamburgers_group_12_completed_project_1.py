'''
IS 303-004 Team 12
    Levi Duke, Dallin Larson, Jarom Mollinet, Ben Roper and Cole Solari
    
Group Project #1: Hamburger Door Dash
'''

# import random function set for randomburgers
import random

class Order:
    def __init__(self):
        # Call randomBurgers() method in constructor, assigning return value to burger_count instance variable
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        # Return a random number between 1 and 20
        for iCount in range(0, 8) :
             return random.randint(1, 20)

#create class: Person
class Person :
  def __init__(self) :
    self.customer_name = self.randomName()

    #create random name method
  def  randomName (self) :

    #assign randomization to the names
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    

    #make new variable customerName and return a random customer name from asCustomers
    return random.choice(asCustomers)

#Create customer class that inherits from person class
class Customer(Person) :
    def __init__(self):
       super().__init__()
       self.order = Order()

#create queue "customers"
queueCustomers = []

#create a dictionary
dictCustomers = {}

#add 100 orders to the queue and add customers to the dictionary if they're not there"
for int in range(100) :
  customer = Customer()
  queueCustomers.append(customer)

#Below will add the customer name in the dictionary if it's not already in there
  if customer.customer_name in dictCustomers :
    dictCustomers[customer.customer_name] += customer.order.burger_count
    
  else:
     dictCustomers[customer.customer_name]= customer.order.burger_count

#Sort the customers in descending order based on burger count
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)

#print the list of customers with their burger count in a table format
for customer in listSortedCustomers :
   print('\n' + customer[0].ljust(19), customer[1])