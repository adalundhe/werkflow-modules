from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class ACMExpiration(BaseModel):
    Value: StrictInt
    Type: Literal['MINUTES', 'HOURS', 'DAYS']
