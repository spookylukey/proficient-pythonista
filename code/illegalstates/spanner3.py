from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Spanner:
    length: float
    mass: float
    size: float | None = None
    max_size: float | None = None

    def __post_init__(self) -> None:
        if self.size is None and self.max_size is None:
            raise AssertionError("Spanner must have at least one of `size` or `max_size` defined")

