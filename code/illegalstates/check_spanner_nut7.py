import math
from typing import assert_never

from .spanner4 import AdjustableSpanner, SingleEndedSpanner, Spanner
from .nuts import Nut


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    match spanner:
        case SingleEndedSpanner(size=size):
            return math.isclose(size, nut.size)
        case AdjustableSpanner(max_size=max_size):
            return max_size >= nut.size
        case _:
            assert_never(spanner)
