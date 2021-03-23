pip install pandas 
import pandas 

class Book:
    def __init__(self, Book_name):
        self.Book_name = Book_name
        self.BuyOrders = []
        self.SellOrders = []
        
    def State_Book_BuySide(self):
        if self.BuyOrders == [] :
          print(" ")
        else:
            for i in range(len(self.BuyOrders)):
                print("BUY ", self.BuyOrders[i].NbrAction,"@", self.BuyOrders[i].Price)
            
    def State_Book_SellSide(self):
        if self.SellOrders == [] :
          print(" ")
        else:
            for i in range(len(self.SellOrders)):
                print("SELL ", self.SellOrders[i].NbrAction,"@", self.SellOrders[i].Price)
                
                
    def log_display(self):
        print("Book on " , self.Book_name, ':\n')
        self.State_Book_BuySide()
        self.State_Book_SellSide()
        print("\n")
        print("---------------------------------------------")
        df=pandas.DataFrame(ar,columns=['Sell', 'Buy']
        
    def HighestBid(self):
        print(self.BuyOrders[0].Price)
        
    def LowestAsk(self):
        print(self.SellOrders[0].Price)
        
        
    def insert_buy(self, NbrAction, Price):
        order = Order(NbrAction, Price, 'Buy')
        print("Insert BUY", order.NbrAction, "@", order.Price, "on", self.Book_name)
        if self.BuyOrders == []:
            self.BuyOrders.append(order)
            self.log_display()
        else:
            for i in range(len(self.BuyOrders)):
                if self.BuyOrders[i].Price < order.Price:
                    self.BuyOrders.insert(i,order)
                    self.log_display()
                    break
                #elif self.BuyOrders[i-1].Price == order.Price and self.BuyOrders[i].Price < order.Price :
                elif self.BuyOrders[i].Price == order.Price:
                    self.BuyOrders.insert(i+1,order)
                    self.log_display()
            if self.BuyOrders[-1].Price > order.Price :
                self.BuyOrders.append(order)
                self.log_display()
        self.order_trades()
            
            
    def insert_sell(self, NbrAction, Price):
        order = Order(NbrAction, Price, 'Sell')
        print("Insert SELL", order.NbrAction, "@", order.Price, "on", self.Book_name)
        if self.SellOrders == []:
            self.SellOrders.append(order)
            self.log_display()
        else:
            for i in range(len(self.SellOrders)):
                if self.SellOrders[i].Price > order.Price:
                    self.SellOrders.insert(i, order)
                    self.log_display()
                    break
                elif self.SellOrders[i].Price == order.Price and self.SellOrders[i+1].Price > order.Price :
                    self.SellOrders.insert(i+1, order)
                    self.log_display()
            if self.SellOrders[-1].Price < order.Price:
                self.SellOrders.append(order)
                self.log_display()
        self.order_trades()
        
    def order_trades(self):
        for i in range(max(len(self.BuyOrders),len(self.SellOrders))):
            if self.BuyOrders != [] and self.SellOrders != []:
                if self.BuyOrders[0].Price >= self.SellOrders[0].Price:
                    if self.BuyOrders[0].NbrAction == self.SellOrders[0].NbrAction:
                        print("Execute ",self.BuyOrders[0].NbrAction, " at ", self.BuyOrders[0].Price , " on " , self.Book_name)
                        del self.BuyOrder[0]
                        del self.SellOrders[0]
                       
                        
                    elif self.BuyOrders[0].NbrAction < self.SellOrders[0].NbrAction:
                        print("Execute ",self.BuyOrders[0].NbrAction, " at ", self.BuyOrders[0].Price , " on " , self.Book_name)
                        self.SellOrders[0].NbrAction = self.SellOrders[0].NbrAction - self.BuyOrders[0].NbrAction
                        del self.BuyOrders[0]
                      
                    elif self.BuyOrders[0].NbrAction > self.SellOrders[0].NbrAction:
                        print("Execute ",self.SellOrders[0].NbrAction, " at ", self.BuyOrders[0].Price , " on " , self.Book_name)                       
                        self.BuyOrders[0].NbrAction= self.BuyOrders[0].NbrAction - self.SellOrders[0].NbrAction
                        del self.SellOrders[0]
                        
                                      
               
        
            
            
            
class Order:
    
    def __init__(self, NbrAction, Price, OrderType):
        self.NbrAction = NbrAction
        self.Price = Price
        self.OrderType = OrderType
