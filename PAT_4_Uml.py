class Customer:
    def __init__(self, ID: int, name: str, discount: int):
        self.ID = ID
        self.name = name
        self.discount = discount

    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def getDiscount(self):
        return self.discount

    def setDiscount(self, discount: int):
        self.discount = discount

    
    def toString(self) -> str:
         return self.name + " (" + str(self.ID) + ")"
   
customer1 = Customer(1001, "Dhivya", 10)
        
print(customer1.ID) 
print(customer1.name)         
print(customer1.discount,"%") 

customer1.discount = 20
print("set the discount :",customer1.discount,"%")   

print(customer1.toString())  

