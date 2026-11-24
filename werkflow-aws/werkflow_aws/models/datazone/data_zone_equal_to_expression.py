from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneEqualToExpression(BaseModel):
    columnName: StrictStr | None = None
    value: StrictStr | None = None
