
import unittest
# Implement the below function and run the program


def are_anagrams(word1, word2):
    return(sorted(word1)==sorted(word2))


class TestAreAnagrams(unittest.TestCase):

    def test_1(self):
        self.assertEqual(are_anagrams('listen', 'silent'), True)

    def test_2(self):
        self.assertEqual(are_anagrams('bedroom', 'bathroom'), False)

    def test_3(self):
        self.assertEqual(are_anagrams('madam', 'madam'), True)

    def test_4(self):
        self.assertEqual(are_anagrams('dabc', 'akbc'), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
