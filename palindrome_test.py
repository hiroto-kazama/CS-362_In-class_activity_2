import unittest
import palindrome

class testPalindrome(unittest.TestCase):
    def test_palindrome(self):
        Var = palindrome.isPalindrome("bob")
        self.assertEqual(Var, True)
        
    def test_palindrome_2(self):
        Var = palindrome.isPalindrome("sing")
        self.assertEqual(Var, False)    

if __name__ == '__main__':
    unittest.main()
