import unittest
from classes import LearningMap
 

class TestMap(unittest.TestCase):
    """Doc String for the class"""

    def setUp(self):
        self.map = LearningMap()
        self.skill = Skill()

    def test_add_skill_success(self):
        """"""
        list_before = len(self.map.skills_list)
        self.map.add_skill(self.skill)
        list_after = len(self.map.skills_list)
        self.assertEqual([list_before, list_after], [0, 1], msg = "skill should be added to the skills_list")

    def test_add_skill_non_string(self):
        """"""
        self.assertRaises(TypeError, self.map.add_skill, 5, msg = "Skill name should be a string")

if __name__ == '__main__':
    unittest.main()