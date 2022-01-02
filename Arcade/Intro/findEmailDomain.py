import re


def findEmailDomain(address):
    return re.findall(r"@([a-zA-Z0-9\-\_]+\.[a-zA-Z]+)", address)[0]
