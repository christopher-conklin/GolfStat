import unittest
import os
from core.Hole import Hole
from core.Course import Tee, Course
from core.Round import Round


test_hole = Hole(par=5,
                 yardage=556,
                 score=4,
                 putts=2,
                 chips=1,
                 fairway_hit=False,
                 fairway_miss='left',
                 green_miss=['short', 'right'],
                 first_putt_length=15,
                 tee_club='D',
                 approach_club=None
                 )

test_tee = Tee(hole=[test_hole]*18)

test_course = Course(name='Palm Dunes Escape',
                     location='Boston, MA',
                     tee={'Copper': test_tee})

test_round = Round().from_course(test_course, 'Copper')


class TestIO(unittest.TestCase):
    def test_hole_to_from_dict(self):
        test_dict = test_hole.as_dict()
        self.assertEqual(test_hole, Hole().from_dict(test_dict))

    def test_tee_to_from_dict(self):
        test_dict = test_tee.as_dict()
        self.assertEqual(test_tee, Tee().from_dict(test_dict))

    def test_course_to_from_file(self):
        filename = 'test_course.json'
        test_course.to_file(filename)
        new_course = Course().from_file(filename)
        os.remove(filename)
        self.assertEqual(test_course, new_course)

    def test_round_to_from_file(self):
        filename = 'test_round.json'
        test_round.to_file(filename)
        new_round = Round().from_file(filename)
        os.remove(filename)
        self.assertEqual(test_round, new_round)






if __name__ == '__main__':
    unittest.main()
