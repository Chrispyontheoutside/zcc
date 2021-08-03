import tickets
import unittest
import json

class Test_tickets(unittest.TestCase):
    def setUp(self):
        self.tickets = tickets.tickets()
        self.tickets.tickets = [json.load(open("test.json",'r'))]

    def test_get_individual_ticket(self):
        self.assertEqual(self.tickets.get_individual_ticket(5),self.tickets.tickets[0]["tickets"][4])
        self.assertEqual(self.tickets.get_individual_ticket(10),self.tickets.tickets[0]["tickets"][9])
        self.assertEqual(self.tickets.get_individual_ticket(15),self.tickets.tickets[0]["tickets"][14])
    def test_get_individual_ticket_outofbounds(self):
        self.assertRaises(IndexError,self.tickets.get_individual_ticket,500)
        self.assertRaises(IndexError,self.tickets.get_individual_ticket,400)
    #If ticketID is passed as string, take as argument
    def test_get_individual_ticket_stringID(self):
        self.assertEqual(self.tickets.get_individual_ticket("5"),self.tickets.tickets[0]["tickets"][4])
        self.assertEqual(self.tickets.get_individual_ticket("10"),self.tickets.tickets[0]["tickets"][9])
    #If a non integer string is passed, raise ValueError
    def test_get_individual_ticket_nonnumerical_string(self):
        self.assertRaises(ValueError,self.tickets.get_individual_ticket,"5f")
        self.assertRaises(ValueError,self.tickets.get_individual_ticket,"9a")
    #Bare method, testing priority is low
    def test_total_tickets(self):
        self.assertEqual(self.tickets.total_tickets(),25)
        for i in range(1,10):
            self.tickets.tickets.append(self.tickets.tickets[-1])
            self.assertEqual(self.tickets.total_tickets(),25+25*i)
