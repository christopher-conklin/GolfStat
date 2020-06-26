import attr
from typing import List

@attr.s
class Hole:
    par: int = attr.ib(default=None)
    yardage: int = attr.ib(default=None)

    score: int = attr.ib(default=None)
    putts: int = attr.ib(default=None)
    chips: int = attr.ib(default=None)
    fairway_hit: bool = attr.ib(default=None)
    fairway_miss: str = attr.ib(default=None)
    green_miss: List[str] = attr.ib(default=None)

    first_putt_length: float = attr.ib(default=None)
    tee_club: str = attr.ib(default=None)
    approach_club: str = attr.ib(default=None)

    def gir(self) -> bool:
        if self.score - self.putts == self.par - 2:
            return True
        else:
            return False

    def scramble(self) -> bool:
        if not self.gir():
            if self.score-self.par <= 0:
                return True

        return False

    def as_dict(self):
        return attr.asdict(self)

    @staticmethod
    def from_dict(h_dict):
        return Hole(**h_dict)
        # return Hole(par=h_dict['par'],
        #             yardage=h_dict['yardage'],
        #             score=h_dict['score'],
        #             putts=h_dict['putts'],
        #             chips=h_dict['chips'],
        #             fairway_hit=h_dict['fairway_hit'],
        #             fairway_miss=h_dict['fairway_miss'],
        #             green_miss=h_dict['green_miss'],
        #             first_putt_length=h_dict['first_putt_length'])

