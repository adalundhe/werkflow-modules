from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_pivot_table_data_path_option import QuickSightPivotTableDataPathOption
from .quick_sight_pivot_table_field_collapse_state_option import QuickSightPivotTableFieldCollapseStateOption
from .quick_sight_pivot_table_field_option import QuickSightPivotTableFieldOption


class QuickSightPivotTableFieldOptions(BaseModel):
    SelectedFieldOptions: list[QuickSightPivotTableFieldOption] | None = None
    DataPathOptions: list[QuickSightPivotTableDataPathOption] | None = None
    CollapseStateOptions: list[QuickSightPivotTableFieldCollapseStateOption] | None = None
