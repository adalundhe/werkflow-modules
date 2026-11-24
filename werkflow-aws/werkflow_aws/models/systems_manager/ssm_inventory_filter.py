from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMInventoryFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
    Type: Literal['Equal', 'NotEqual', 'BeginWith', 'LessThan', 'GreaterThan', 'Exists'] | None = None
