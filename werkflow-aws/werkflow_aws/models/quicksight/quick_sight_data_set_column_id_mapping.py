from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetColumnIdMapping(BaseModel):
    SourceColumnId: StrictStr | None = None
    TargetColumnId: StrictStr | None = None
