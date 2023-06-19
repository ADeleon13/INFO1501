from rectangle import Rectangle


class Carpet(Rectangle):
    def __init__(self, Length, Width, PPS):
        Rectangle.__init__(self, Length, Width)
        self.pricePerSquareFoot = PPS

    def get_Price(self):
        return self.get_area() * self.pricePerSquareFoot


    def __str__(self):
        returnStr = "Carpet Details: \n\tRectangle:{0} \n\tPrice/SQft:{2} \n\tTotal Price:{1}"
        return returnStr.format(Rectangle.__str__(self), self.get_Price(), self.pricePerSquareFoot)

