import os


class SecretAuction:
    __bidders: dict

    def __init__(self):
        self.__bidders = {}

    def start(self):
        print("Bienvenido a la subasta!")
        another_bidder = True
        while another_bidder:
            name = input("\nNombre: ")
            if not name.isalpha():
                print("Nombre no válido.")
                continue

            bid = None
            try:
                bid = float(input("Oferta: "))
            except ValueError:
                print("Oferta no válida.")
                continue

            self.__bidders[name] = bid

            another_bidder = input("\n¿Hay otra persona ofertando? [si/no]: ") == "si"
            os.system("clear")
        self.finish()

    def finish(self):
        winner_bid = self.get_max_biller()
        print(f"\n{winner_bid} ganó con una oferta de ${self.__bidders[winner_bid]}")

    def get_max_biller(self):
        max_bidder = None
        max_bid = 0
        for k, v in self.__bidders.items():
            if v > max_bid:
                max_bid = v
                max_bidder = k
        return max_bidder


if __name__ == "__main__":
    sa = SecretAuction()
    sa.start()
