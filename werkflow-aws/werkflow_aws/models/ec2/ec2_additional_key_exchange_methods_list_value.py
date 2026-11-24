from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2AdditionalKeyExchangeMethodsListValue(BaseModel):
    Value: StrictInt | None = None
