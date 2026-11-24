from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_table_field_subtotal_options import QuickSightPivotTableFieldSubtotalOptions
from .quick_sight_table_cell_style import QuickSightTableCellStyle
from .quick_sight_table_style_target import QuickSightTableStyleTarget


class QuickSightSubtotalOptions(BaseModel):
    TotalsVisibility: StrictStr | None = None
    CustomLabel: StrictStr | None = None
    FieldLevel: StrictStr | None = None
    FieldLevelOptions: list[QuickSightPivotTableFieldSubtotalOptions] | None = None
    TotalCellStyle: QuickSightTableCellStyle | None = None
    ValueCellStyle: QuickSightTableCellStyle | None = None
    MetricHeaderCellStyle: QuickSightTableCellStyle | None = None
    StyleTargets: list[QuickSightTableStyleTarget] | None = None
