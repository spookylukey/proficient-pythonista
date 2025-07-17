from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class SpannerCommon:
    length: float
    mass: float


@dataclass(frozen=True, kw_only=True)
class SingleEndedSpanner(SpannerCommon):
    size: float


@dataclass(frozen=True, kw_only=True)
class AdjustableSpanner(SpannerCommon):
    max_size: float


type Spanner = SingleEndedSpanner | AdjustableSpanner
