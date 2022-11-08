import unittest
from app.services.create_account_service.app import create_func
class Test(unittest.TestCase):
    def test_pass_1(self):
        username = 'admin'
        password = 'admin'
        result = create_func(username, password)
        expec = {'SUCCESS': 'Create Successful',
                f'{username}': f'{password}'}
        self.assertEqual(result['SUCCESS'],expec['SUCCESS'])
        self.assertEqual(result[f'{username}'],expec[f'{username}'])
    
    def test_pass_2(self):
        username = 'admin'
        password = None
        result = create_func(username, password)
        expec = {'FAILED': 'Create Failed'}
        self.assertEqual(result['FAILED'],expec['FAILED'])

    def test_pass_3(self):
        username = None
        password = '123'
        result = create_func(username, password)
        expec = {'FAILED': 'Create Failed'}
        self.assertEqual(result['FAILED'],expec['FAILED'])

if __name__ == "__main__":
    unittest.main(Test())