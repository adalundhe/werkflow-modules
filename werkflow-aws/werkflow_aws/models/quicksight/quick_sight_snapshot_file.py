from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_snapshot_file_sheet_selection import QuickSightSnapshotFileSheetSelection


class QuickSightSnapshotFile(BaseModel):
    SheetSelections: list[QuickSightSnapshotFileSheetSelection] | None = None
    FormatType: StrictStr | None = None
