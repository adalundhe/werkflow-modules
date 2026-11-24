from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDateTimeCondition(BaseModel):
    FieldName: StrictStr | None = None
    MinValue: StrictStr | None = None
    MaxValue: StrictStr | None = None
    ComparisonType: Literal['GREATER_THAN', 'LESS_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN_OR_EQUAL_TO', 'EQUAL_TO', 'RANGE'] | None = None
