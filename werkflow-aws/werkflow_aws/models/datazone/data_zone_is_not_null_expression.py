from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneIsNotNullExpression(BaseModel):
    columnName: StrictStr | None = None
