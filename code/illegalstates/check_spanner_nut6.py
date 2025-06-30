import math
from typing import assert_never

from .spanner4 import AdjustableSpanner, SingleEndedSpanner, Spanner
from .nuts import Nut


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    if isinstance(spanner, SingleEndedSpanner):
        return math.isclose(spanner.size, nut.size)
    if isinstance(spanner, AdjustableSpanner):
        return spanner.max_size >= nut.size
    assert_never(spanner)
