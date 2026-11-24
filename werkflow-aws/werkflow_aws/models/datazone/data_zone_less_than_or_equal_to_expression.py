from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneLessThanOrEqualToExpression(BaseModel):
    columnName: StrictStr | None = None
    value: StrictStr | None = None
