from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDateCondition(BaseModel):
    FieldName: StrictStr | None = None
    Value: StrictStr | None = None
    ComparisonType: Literal['GREATER_THAN', 'LESS_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN_OR_EQUAL_TO', 'EQUAL_TO'] | None = None
