from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexIntentFilter(BaseModel):
    name: Literal['IntentName']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
