from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightCascadingControlSource(BaseModel):
    SourceSheetControlId: StrictStr | None = None
    ColumnToMatch: QuickSightColumnIdentifier | None = None
