import unittest
from script import processFile
class Testing(unittest.TestCase):
    
    def test_file_1(self):
        file = open("resources/calendar1.csv","r")
        response = processFile(file)
        file.close()
        b = {('ASTRID', 'ANDRES'): 3, ('RENE', 'ANDRES'): 2, ('RENE', 'ASTRID'): 2}
        self.assertEqual(response, b)
        
    def test_file_2(self):
        file = open("resources/calendar2.csv","r")
        response = processFile(file)
        file.close()
        b = {('RENE', 'ASTRID'): 3, ('RENE', 'ANDRES'): 3, ('ASTRID', 'ANDRES'): 3}
        self.assertEqual(response, b)

    def test_file_3(self):
        file = open("resources/calendar3.csv","r")
        response = processFile(file)
        file.close()
        b = {('RENE', 'ASTRID'): 2, ('ASTRID', 'ANDRES'): 2, ('RENE', 'ANDRES'): 1}
        self.assertEqual(response, b)
    
    def test_wrong_time_formar(self):
        file = open("resources/calendar_wrong_time_format.csv","r")
        response = processFile(file)
        file.close()
        b = None
        self.assertEqual(response, b)

if __name__ == '__main__':
    unittest.main()