from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftModifyUsageLimitRequest(BaseModel):
    UsageLimitId: StrictStr
    Amount: StrictInt | None = None
    BreachAction: Literal['log', 'emit-metric', 'disable'] | None = None
