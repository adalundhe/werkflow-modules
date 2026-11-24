from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMOpsItemFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
    Operator: Literal['Equal', 'Contains', 'GreaterThan', 'LessThan']
