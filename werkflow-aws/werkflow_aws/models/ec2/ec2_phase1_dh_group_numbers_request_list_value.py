from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2Phase1DHGroupNumbersRequestListValue(BaseModel):
    Value: StrictInt | None = None
