from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class EC2ReservedInstanceLimitPrice(BaseModel):
    Amount: StrictFloat | StrictInt | None = None
    CurrencyCode: Literal['USD'] | None = None
