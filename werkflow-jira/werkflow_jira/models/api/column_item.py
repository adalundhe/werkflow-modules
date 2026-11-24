from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ColumnItem(BaseModel):
    label: StrictStr | None = None
    value: StrictStr | None = None
