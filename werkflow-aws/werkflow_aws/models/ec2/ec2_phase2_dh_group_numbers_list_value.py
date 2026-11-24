from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2Phase2DHGroupNumbersListValue(BaseModel):
    Value: StrictInt | None = None
