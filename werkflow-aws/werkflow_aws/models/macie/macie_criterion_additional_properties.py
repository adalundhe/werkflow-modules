from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieCriterionAdditionalProperties(BaseModel):
    eq: list[StrictStr] | None = None
    eqExactMatch: list[StrictStr] | None = None
    gt: StrictInt | None = None
    gte: StrictInt | None = None
    lt: StrictInt | None = None
    lte: StrictInt | None = None
    neq: list[StrictStr] | None = None
