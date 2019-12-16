class Location:
    
    # def __init__(self, **kwargs):
    #     self.address = kwargs.get('address')

    def __init__(self, address):
        self.address = address


    def __repr__(self):
        return f"<{type(self).__name__} {self.__dict__}>"



# print(Location("1261 Wild Azalea Ln."))