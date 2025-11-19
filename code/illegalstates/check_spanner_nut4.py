import math

from .nuts import Nut
from .spanner2 import Spanner


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    if isinstance(spanner.size, float):
        return math.isclose(spanner.size, nut.size)
    if isinstance(spanner.max_size, float):
        return spanner.max_size >= nut.size
    raise AssertionError("Spanner must have at least one of `size` or `max_size` defined")
