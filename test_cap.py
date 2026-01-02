import unittest
import cap

class TestCap(unittest.TestCase): #inherit from the uniitest class -> subpackage TestCase
    def test_one_word(self):
        text='python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python') #check if both are equal

    def test_multiple_words(self):
        text="syed shaista"
        result = cap.cap_text(text)
        self.assertEqual(result,'Syed Shaista')

if __name__ == '__main__':
    unittest.main()