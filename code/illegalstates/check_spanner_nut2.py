import math

from .spanner2 import Spanner
from .nuts import Nut


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    return math.isclose(spanner.size, nut.size)
