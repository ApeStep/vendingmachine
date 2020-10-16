from abc import ABC, abstractmethod

class Payment(ABC):
    # @abstractmethod
    # def connect(self):
    #     pass

    # @abstractmethod
    # def disconnect(self):
    #     pass

    @abstractmethod
    def startPayment(self, amount: float) -> int:
        pass

    @abstractmethod
    def validatePayment(self, id: int) -> bool:
        pass

    @abstractmethod
    def cancelPayment(self, id: int):
        pass