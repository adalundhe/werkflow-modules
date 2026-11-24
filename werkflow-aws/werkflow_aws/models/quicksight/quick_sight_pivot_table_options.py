from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_table_rows_label_options import QuickSightPivotTableRowsLabelOptions
from .quick_sight_row_alternate_color_options import QuickSightRowAlternateColorOptions
from .quick_sight_table_cell_style import QuickSightTableCellStyle


class QuickSightPivotTableOptions(BaseModel):
    MetricPlacement: StrictStr | None = None
    SingleMetricVisibility: StrictStr | None = None
    ColumnNamesVisibility: StrictStr | None = None
    ToggleButtonsVisibility: StrictStr | None = None
    ColumnHeaderStyle: QuickSightTableCellStyle | None = None
    RowHeaderStyle: QuickSightTableCellStyle | None = None
    CellStyle: QuickSightTableCellStyle | None = None
    RowFieldNamesStyle: QuickSightTableCellStyle | None = None
    RowAlternateColorOptions: QuickSightRowAlternateColorOptions | None = None
    CollapsedRowDimensionsVisibility: StrictStr | None = None
    RowsLayout: StrictStr | None = None
    RowsLabelOptions: QuickSightPivotTableRowsLabelOptions | None = None
    DefaultCellWidth: StrictStr | None = None
