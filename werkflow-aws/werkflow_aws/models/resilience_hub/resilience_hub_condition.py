from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ResilienceHubCondition(BaseModel):
    field: StrictStr
    operator: Literal['Equals', 'NotEquals', 'GreaterThen', 'GreaterOrEquals', 'LessThen', 'LessOrEquals']
    value: StrictStr | None = None
