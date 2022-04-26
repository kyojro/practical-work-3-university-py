import sys

# 1$ = 32.5  1€ = 33.9 1zł = 6.8 (UAH)
price = {"bread": 0.4, "milk": 0.5, "meat": 2, "potato": 0.7}


class Exchange:
    @staticmethod
    def usd():
        new_price = {i: round(price[i] * float(sys.argv[2]), 2) for i in price}
        with open("usd.md", 'w') as f:
            for key, value in new_price.items():
                f.write(f"{key} = {value} UAH (if 1 USD = {sys.argv[2]})\n")
        f = open("usd.md")
        ff = f.read()
        f.close()
        print(ff)

    @staticmethod
    def eur():
        new_price = {i: round(price[i] * float(sys.argv[2]), 2) for i in price}
        with open("eur.md", 'w') as f:
            for key, value in new_price.items():
                f.write(f"{key} = {value} UAH (if 1 EUR = {sys.argv[2]})\n")
        f = open("eur.md")
        ff = f.read()
        f.close()
        print(ff)

    @staticmethod
    def pln():
        new_price = {i: round(price[i] * float(sys.argv[2]), 2) for i in price}
        with open("pln.md", 'w') as f:
            for key, value in new_price.items():
                f.write(f"{key} = {value} UAH (if 1 PLN = {sys.argv[2]})\n")
        f = open("pln.md")
        ff = f.read()
        f.close()
        print(ff)


x = Exchange()
if sys.argv[1] == "usd":
    x.usd()
if sys.argv[1] == "eur":
    x.eur()
if sys.argv[1] == "pln":
    x.pln()
