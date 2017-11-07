from unittest import TestCase
def find_all_pallindrome_numbers():
    for num in range(1000, 10000):
        num_rev = int(str(num)[::-1])
        if num * 4 == num_rev:
            return num


x = find_all_pallindrome_numbers()
print(x)


class TestFind_all_pallindrome_numbers(TestCase):
    def test_find_all_pallindrome_numbers(self):
        self.assertEqual(find_all_pallindrome_numbers(), 2178)


import unittest

if __name__ == "main":
    unittest.main()
