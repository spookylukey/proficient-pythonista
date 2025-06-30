from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class SpannerCommon:
    length: float
    mass: float


@dataclass(frozen=True, kw_only=True)
class SingleEndedSpanner:
    size: float


@dataclass(frozen=True, kw_only=True)
class AdjustableSpanner:
    max_size: float


type Spanner = SingleEndedSpanner | AdjustableSpanner
