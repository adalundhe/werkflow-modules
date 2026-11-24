from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class EC2PriceScheduleSpecification(BaseModel):
    Term: StrictInt | None = None
    Price: StrictFloat | StrictInt | None = None
    CurrencyCode: Literal['USD'] | None = None
