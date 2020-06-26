import unittest
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


class TestRound(unittest.TestCase):
    def test_round_from_course(self):
        test_round = Round(course=test_course.name,
                           location=test_course.location,
                           tee='Copper',
                           hole=test_course.tee['Copper'])
        self.assertEqual(test_round, Round().from_course(test_course, 'Copper'))


if __name__ == '__main__':
    unittest.main()
