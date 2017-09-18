from unittest import TestCase

from arithmeticskill.arithmeticskill import ArithmeticSkill



class BaseTest(TestCase):

    def setUp(self):
        self.skill = ArithmeticSkill()



class ArithmeticSkillTest(BaseTest):
    def test_plus(self):
        results = self.skill.solve(2,'plus',3);
        self.assertIsEqual(results,5)
    def test_minus(self):
        results = self.skill.solve(2,'minus',3);
        self.assertIsEqual(results,-1)
    def test_multiply(self):
        results = self.skill.solve(2,'multiplied by',3);
        self.assertIsEqual(results,6)
    def test_divide(self):
        results = self.skill.solve(4,'divided by',2);
        self.assertIsEqual(results,2)
    def test_badopp(self):
        results = self.skill.solve(4,'cushioned by',2);
        self.assertIsNone(results)
