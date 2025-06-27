from dataclasses import dataclass


@dataclass
class Spanner:
    length: float
    mass: float
    size: float | None = None
    max_size: float | None = None
