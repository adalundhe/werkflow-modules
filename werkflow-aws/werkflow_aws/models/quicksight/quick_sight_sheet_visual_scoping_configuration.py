from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetVisualScopingConfiguration(BaseModel):
    SheetId: StrictStr | None = None
    Scope: StrictStr | None = None
    VisualIds: list[StrictStr] | None = None
