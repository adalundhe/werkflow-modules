from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectDecimalCondition(BaseModel):
    FieldName: StrictStr | None = None
    MinValue: StrictFloat | StrictInt | None = None
    MaxValue: StrictFloat | StrictInt | None = None
    ComparisonType: Literal['GREATER_OR_EQUAL', 'GREATER', 'LESSER_OR_EQUAL', 'LESSER', 'EQUAL', 'NOT_EQUAL', 'RANGE'] | None = None
