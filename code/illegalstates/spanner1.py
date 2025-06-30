from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Spanner:
    size: float
    length: float
    mass: float
