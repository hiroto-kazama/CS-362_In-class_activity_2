import unittest
import word_count

class testWord_count(unittest.TestCase):
    def test_word_count(self):
        Var = word_count.wordCount("hiroto kazama")
        self.assertEqual(Var, 2)

    def test_word_count_2(self):
        Var = word_count.wordCount("test test test test")
        self.assertEqual(Var, 4)


if __name__ == '__main__':
    unittest.main()
