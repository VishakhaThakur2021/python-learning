#method overriding- child class implement or reuse or overrides its parent method

class Hotel:
    def dinner(self):
        print("dinner is ready")

class Resturant(Hotel):
    def dinner(self):    # child class is overriding parent method
        print("serve the dinner in restro")

resturant =Resturant()
resturant.dinner()