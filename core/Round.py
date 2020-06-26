import attr
import json
from core.Hole import Hole
from datetime import datetime
from core.Course import Tee, Course
from copy import deepcopy


@attr.s
class Round(Tee):
    course: str = attr.ib(default=None)
    tee: str = attr.ib(default=None)
    location = attr.ib(default=None)
    date = attr.ib(default=datetime.now())

    def to_file(self, filename):
        out_dict = attr.asdict(self)
        out_dict['date'] = datetime.timestamp(self.date)
        with open(filename, 'w') as f:
            json.dump(out_dict, f)

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as f:
            in_dict = json.load(f)
        return Round(course=in_dict['course'],
                     tee=in_dict['tee'],
                     location=in_dict['location'],
                     hole=[Hole().from_dict(hd) for hd in in_dict['hole']],
                     date=datetime.fromtimestamp(in_dict['date']))

    @staticmethod
    def from_course(course: Course, tee_name: str):
        return Round(course=course.name,
                     tee=tee_name,
                     location=course.location,
                     hole=deepcopy(course.tee[tee_name].hole))
