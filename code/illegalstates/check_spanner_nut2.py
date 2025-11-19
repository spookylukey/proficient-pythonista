import math

from .nuts import Nut
from .spanner2 import Spanner


def does_spanner_fit_nut(spanner: Spanner, nut: Nut) -> bool:
    return math.isclose(spanner.size, nut.size)
