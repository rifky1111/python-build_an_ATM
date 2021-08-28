

class Customer:
    def __init__(self,id,custPin = 1234,custBalance = 10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def checkId(self):
        return self.id
    def checkPin(self):
        return self.custPin
    def checkBalance(self):
        return self.custBalance

    def debet(self,nominal):
        self.custBalance -= nominal
        return self.custBalance
    def simpan(self,nominal):
        self.custBalance += nominal
        return self.custBalance 
