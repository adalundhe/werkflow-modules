from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectStringCondition(BaseModel):
    FieldName: StrictStr | None = None
    Value: StrictStr | None = None
    ComparisonType: Literal['STARTS_WITH', 'CONTAINS', 'EXACT'] | None = None
