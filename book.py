class Order():

    def __init__(self, quantity, price, buy=True): 
        self.quantity=quantity
        self.price=price
        self.buy = buy 

    def is_sell(self): 
        return not self.buy

    def __affichage__(self): 
        return "Order(%s, %s)" % (self.quantity, self.price)
  
    
   
class Book(): 
    
    def __init__(self, name, sell=[], buy=[]):
        self.name=name
        self.sell=sell 
        self.buy=buy


    def insert_buy(): 

        def insert_sell():

