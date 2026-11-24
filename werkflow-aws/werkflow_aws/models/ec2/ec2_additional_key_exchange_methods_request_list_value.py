from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2AdditionalKeyExchangeMethodsRequestListValue(BaseModel):
    Value: StrictInt | None = None
