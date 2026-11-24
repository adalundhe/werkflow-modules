from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessPermissionCondition(BaseModel):
    conditionOperator: Literal['StringEquals']
    conditionKey: StrictStr
    conditionValues: list[StrictStr]
