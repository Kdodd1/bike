class bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print(("This bike is $")+ str(self.price) + ("\n The max speed is: ") 
        + self.max_speed + ("\n It has ") + str(self.miles) + (" miles on it"))
        return self
    
    def ride(self):
        self.miles +=10
        print("Riding")
        return self
        
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 =bike(100, "25mph", 0)
bike2 = bike(150, "30mph", 0)
bike3 = bike(90, "20mph", 0)

bike1.ride().ride().ride().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()




