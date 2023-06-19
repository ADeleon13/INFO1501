from rectangle import Rectangle


class Rug(Rectangle):
    def __init__(self, Length, Width, price):
        Rectangle.__init__(self, Length, Width)
        self.price = price

    def get_Price(self):
        return self.price

    def __str__(self):
        returnStr= "Rug details: \n\tRectangle:{} \n\tPrice {} "
        return returnStr.format(Rectangle.__str__(self), self.price)
