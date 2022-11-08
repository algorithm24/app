import unittest
from app.services.login_service.app import login_func

class Test(unittest.TestCase):
    def test_pass_1(self):
        username = 'admin'
        password = 'admin'
        result = login_func(username, password)
        expec = {'SUCCESS': 'Login Successful',
                f'{username}': f'{password}'}
        self.assertEqual(result['SUCCESS'],expec['SUCCESS'])
        self.assertEqual(result[f'{username}'],expec[f'{username}'])
    
    def test_pass_2(self):
        username = 'admin'
        password = '123'
        result = login_func(username, password)
        expec = {'FAILED': 'Login Failed'}
        self.assertEqual(result['FAILED'],expec['FAILED'])

if __name__ == "__main__":
    unittest.main(Test())