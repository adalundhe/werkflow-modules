from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_table_cell_style import QuickSightTableCellStyle
from .quick_sight_total_aggregation_option import QuickSightTotalAggregationOption


class QuickSightPivotTotalOptions(BaseModel):
    TotalsVisibility: StrictStr | None = None
    Placement: StrictStr | None = None
    ScrollStatus: StrictStr | None = None
    CustomLabel: StrictStr | None = None
    TotalCellStyle: QuickSightTableCellStyle | None = None
    ValueCellStyle: QuickSightTableCellStyle | None = None
    MetricHeaderCellStyle: QuickSightTableCellStyle | None = None
    TotalAggregationOptions: list[QuickSightTotalAggregationOption] | None = None
