import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self_customer_1 = Customer('John', 'Brad', 5000)
        self_customer_2 = Customer('Tina', 'Smith', 3000)

    def test_customer_mail(self):
        self.assertEqual(self.customer_1.customer_mail,'John.Brad@mail.com')
        self.assertEqual(self.customer_2.customer_mail, 'Tina.Smith@mail.com')

    def test_customer_fullname(self):
        self.assertEqual(self.customer_1.fullname, 'John Brad')
        self.assertEqual(self.customer_2.fullname, 'Tina Smith')

    def test_apply_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertEqual(self.customer_1.purchase, 4750)
        self.aseertEqual(self.customer_2.purchase, 2850)

if __name__ == '__main__':
    unittest.main()
        
