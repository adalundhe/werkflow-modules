from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneIsNullExpression(BaseModel):
    columnName: StrictStr | None = None
