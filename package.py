carriers = []

class Package:
    def __init__(self, id):
        self.id = id
        self.carrier = None

    def find_carrier(self):
        pass

    def track(self):
        if not self.carrier:
            self.find_carrier()
        return self.carrier.track(self.id)

