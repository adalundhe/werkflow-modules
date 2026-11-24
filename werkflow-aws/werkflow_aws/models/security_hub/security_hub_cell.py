from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubCell(BaseModel):
    Column: StrictInt | None = None
    Row: StrictInt | None = None
    ColumnName: StrictStr | None = None
    CellReference: StrictStr | None = None
