from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectBooleanCondition(BaseModel):
    FieldName: StrictStr | None = None
    ComparisonType: Literal['IS_TRUE', 'IS_FALSE'] | None = None
