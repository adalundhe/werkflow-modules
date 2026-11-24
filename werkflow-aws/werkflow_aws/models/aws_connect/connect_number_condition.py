from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectNumberCondition(BaseModel):
    FieldName: StrictStr | None = None
    MinValue: StrictInt | None = None
    MaxValue: StrictInt | None = None
    ComparisonType: Literal['GREATER_OR_EQUAL', 'GREATER', 'LESSER_OR_EQUAL', 'LESSER', 'EQUAL', 'NOT_EQUAL', 'RANGE'] | None = None
