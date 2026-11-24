from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMInstancePropertyStringFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
    Operator: Literal['Equal', 'NotEqual', 'BeginWith', 'LessThan', 'GreaterThan'] | None = None
