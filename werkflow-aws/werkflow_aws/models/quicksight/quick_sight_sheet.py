from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_sheet_image import QuickSightSheetImage


class QuickSightSheet(BaseModel):
    SheetId: StrictStr | None = None
    Name: StrictStr | None = None
    Images: list[QuickSightSheetImage] | None = None
