from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_default_new_sheet_configuration import QuickSightDefaultNewSheetConfiguration


class QuickSightAnalysisDefaults(BaseModel):
    DefaultNewSheetConfiguration: QuickSightDefaultNewSheetConfiguration | None = None
