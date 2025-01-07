from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass


class creditCardPayment(PaymentMethod):
    def processPayment(self,Amount):
        print(f"payment of {Amount} paid through Credit card")
        
class payPal(PaymentMethod):
    def processPayment(self,Amount):
         print(f"payment of {Amount} paid through paypal")

fpay = creditCardPayment()
sPay = payPal()

fpay.processPayment(100)
sPay.processPayment(450)

        