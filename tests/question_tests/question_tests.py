#write function tests here, don't add input('') statements here!
from contextlib import nullcontext
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_sum_of_evens, test_config
from src.question_b.question_b import use_global

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_questions_a_sum(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)
    
    def test_question_b(self):
        use_global = "Changed value"
        self.assertEqual (use_global, "Changed value")


