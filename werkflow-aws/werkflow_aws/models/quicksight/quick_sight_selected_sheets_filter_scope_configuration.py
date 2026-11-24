from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_sheet_visual_scoping_configuration import QuickSightSheetVisualScopingConfiguration


class QuickSightSelectedSheetsFilterScopeConfiguration(BaseModel):
    SheetVisualScopingConfigurations: list[QuickSightSheetVisualScopingConfiguration] | None = None
