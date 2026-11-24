from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightOutputColumnNameOverride(BaseModel):
    SourceColumnName: StrictStr | None = None
    OutputColumnName: StrictStr | None = None
