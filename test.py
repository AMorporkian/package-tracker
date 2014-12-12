import unittest
import carriers
import carrier


class TestPackageMatching(unittest.TestCase):
    def setUp(self):
        self.ups = carriers.UPS()
        self.usps = carriers.USPS()
        self.fedex = carriers.FedEx()
        self.carrier = carrier.Carrier()

    def test_valid_matches(self):
        usps_numbers = ["9405510200828317887291", "9400109699938544339782"]
        ups_numbers = ["1Z868YE40326534056", "1Z21E95F0325613424"]
        fedex_numbers = ["590430171251", "588968277777717"]
        self.assertTrue(all([self.ups.match_package(x) for x in ups_numbers]))
        self.assertFalse(any([self.ups.match_package(x) for x in usps_numbers]))
        self.assertFalse(any([self.ups.match_package(x) for x in fedex_numbers]))

        self.assertTrue(all([self.usps.match_package(x) for x in usps_numbers]))
        self.assertFalse(any([self.usps.match_package(x) for x in ups_numbers]))
        self.assertFalse(any([self.usps.match_package(x) for x in fedex_numbers]))

        self.assertTrue(all([self.fedex.match_package(x) for x in fedex_numbers]))
        self.assertFalse(any([self.fedex.match_package(x) for x in ups_numbers]))
        self.assertFalse(any([self.fedex.match_package(x) for x in usps_numbers]))