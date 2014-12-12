from carriers import UPS, USPS, FedEx


class Package:
    def __init__(self, id):
        self.id = id

    def find_carrier(self):
        pass