from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyCondition(BaseModel):
    Eq: list[StrictStr] | None = None
    Neq: list[StrictStr] | None = None
    Gt: StrictInt | None = None
    Gte: StrictInt | None = None
    Lt: StrictInt | None = None
    Lte: StrictInt | None = None
    Equals: list[StrictStr] | None = None
    NotEquals: list[StrictStr] | None = None
    GreaterThan: StrictInt | None = None
    GreaterThanOrEqual: StrictInt | None = None
    LessThan: StrictInt | None = None
    LessThanOrEqual: StrictInt | None = None
    Matches: list[StrictStr] | None = None
    NotMatches: list[StrictStr] | None = None
