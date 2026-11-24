from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneLikeExpression(BaseModel):
    columnName: StrictStr | None = None
    value: StrictStr | None = None
