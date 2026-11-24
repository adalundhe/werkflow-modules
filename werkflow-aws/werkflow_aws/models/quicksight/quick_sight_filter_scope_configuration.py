from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_all_sheets_filter_scope_configuration import QuickSightAllSheetsFilterScopeConfiguration
from .quick_sight_selected_sheets_filter_scope_configuration import QuickSightSelectedSheetsFilterScopeConfiguration


class QuickSightFilterScopeConfiguration(BaseModel):
    SelectedSheets: QuickSightSelectedSheetsFilterScopeConfiguration | None = None
    AllSheets: QuickSightAllSheetsFilterScopeConfiguration | None = None
