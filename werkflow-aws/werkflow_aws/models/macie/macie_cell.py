from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieCell(BaseModel):
    cellReference: StrictStr | None = None
    column: StrictInt | None = None
    columnName: StrictStr | None = None
    row: StrictInt | None = None
