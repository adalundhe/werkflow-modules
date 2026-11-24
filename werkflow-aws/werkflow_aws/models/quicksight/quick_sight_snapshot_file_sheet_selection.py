from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSnapshotFileSheetSelection(BaseModel):
    SheetId: StrictStr | None = None
    SelectionScope: StrictStr | None = None
    VisualIds: list[StrictStr] | None = None
