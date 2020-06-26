import attr
import json
from core.Hole import Hole
from typing import List, Dict


@attr.s
class Tee:
    hole: List[Hole] = attr.ib(default=[Hole()] * 18)

    def as_dict(self) -> dict:
        return attr.asdict(self)

    @staticmethod
    def from_dict(t_dict: dict):
        return Tee(hole=[Hole().from_dict(hd) for hd in t_dict['hole']])


@attr.s
class Course:
    name: str = attr.ib(default=None)
    location = attr.ib(default=None)
    tee: Dict[str, Tee] = attr.ib(default=None)

    def to_file(self, filename):
        out_dict = attr.asdict(self)
        with open(filename, 'w') as f:
            json.dump(out_dict, f)

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as f:
            in_dict = json.load(f)
        return Course(name=in_dict['name'],
                      tee={k: Tee().from_dict(v) for k, v in in_dict['tee'].items()},
                      location=in_dict['location'])
