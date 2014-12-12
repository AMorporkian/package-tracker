from carrier import Carrier


class UPS(Carrier):
    match_regex = r"^1Z"


class USPS(Carrier):
    match_regex = r"^\d{22}|[0-9A-Z]{11}US$"


class FedEx(Carrier):
    match_regex = r"^\d{12,19}$"