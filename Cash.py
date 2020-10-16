from coin_machine import IKEAMyntAtare2000
from tkinter import messagebox
from Payment import Payment

class Cash(Payment):
    def __init__(self):
        self._IKEAMyntAtare2000 = IKEAMyntAtare2000()

    def startPayment(selft):
        messagebox.showinfo(message = "Connecting to card reader...")

    def validatePayment(self, amount: float) -> int:
        self._IKEAMyntAtare2000.betala(amount)

        messagebox.showinfo(message = f"End transaction 1")
        return True

    def cancelPayment(self, id: int):
        if id != 1:
            raise Exception ("Incorrect transaction id")

        messagebox.showinfo(message = "Cancel transaction 1")
