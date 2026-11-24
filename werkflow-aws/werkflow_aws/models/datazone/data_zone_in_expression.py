from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneInExpression(BaseModel):
    columnName: StrictStr | None = None
    values: list[StrictStr] | None = None
