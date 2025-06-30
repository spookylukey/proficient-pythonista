from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Spanner:
    length: float
    mass: float
    size: float | None = None
    max_size: float | None = None
