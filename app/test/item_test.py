import unittest
from app.services.item_service.app import item_func

class Test(unittest.TestCase):
    def test_pass_1(self):
        uuid = '-1'
        result = item_func(uuid)
        expec = {'SUCCESS': 'wrong item!'}
        self.assertEqual(result['SUCCESS'],expec['SUCCESS'])
    
    def test_pass_2(self):
        uuid = '0'
        result = item_func(uuid)
        expec = {'SUCCESS': '0'}
        self.assertEqual(result['SUCCESS'],expec['SUCCESS'])

if __name__ == "__main__":
    unittest.main(Test())