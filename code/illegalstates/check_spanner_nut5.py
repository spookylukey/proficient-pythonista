import math

from .nuts import Nut
from .spanner4 import AdjustableSpanner, SingleEndedSpanner, Spanner


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    if isinstance(spanner, SingleEndedSpanner):
        return math.isclose(spanner.size, nut.size)
    if isinstance(spanner, AdjustableSpanner):
        return spanner.max_size >= nut.size
