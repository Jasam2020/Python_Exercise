import unittest
import Scripts.test1 as my_script

class Testing(unittest.TestCase):
    """def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)
    """
    def test_count_numbers(self):
        result = my_script.count_numbers(2, 2)
        self.assertEqual(result, 4)

    def test_count_only_takes_numbers_as_parameter(self):
        self.assertRaises(TypeError, my_script.count_numbers("a", 3))

    def test_that_counting_float_is_ok(self):
        result = my_script.count_numbers(2.1, 3.4)
        self.assertEqual(result, 5.5)

if __name__ == '__main__':
    unittest.main()
