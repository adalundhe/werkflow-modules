from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class EC2PriceSchedule(BaseModel):
    Active: StrictBool | None = None
    CurrencyCode: StrictStr | None = None
    Price: StrictFloat | StrictInt | None = None
    Term: StrictInt | None = None
