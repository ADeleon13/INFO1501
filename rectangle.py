class Rectangle:
    def __init__(self, Length, Width):
        self.length = Length
        self.width = Width

    def get_length(self):
        return self.length

    def set_length(self, new_length):
        self.length = new_length

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return self.length * self.width


    def __str__(self):
        returnStr= "Length: {} Width: {} Area: {} "
        return returnStr.format(self.length,self.width, self.get_area())