from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightGroupSearchFilter(BaseModel):
    Operator: Literal['StartsWith']
    Name: Literal['GROUP_NAME']
    Value: StrictStr
