from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRenameColumnOperation(BaseModel):
    ColumnName: StrictStr | None = None
    NewColumnName: StrictStr | None = None
