#write function tests here, don't add input('') statements here!
from contextlib import nullcontext
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_sum_of_evens, test_config
from src.question_b.question_b import use_global
from src.question_c.question_c import use_local_variable
from src.question_d.question_d import get_assessment_value, get_tax_assessement_value

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_questions_a(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)
    
    def test_question_b(self):
        use_global = "Changed value"
        self.assertEqual (use_global, "Changed value")

    def test_question_c(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)

    def test_question_d(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

        self.assertEqual(get_tax_assessement_value(6000), 43.20)
        self.assertEqual(get_tax_assessement_value(10000), 72)


        


