from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dashboard_customization_visual_options import QuickSightDashboardCustomizationVisualOptions
from .quick_sight_pivot_table_field_options import QuickSightPivotTableFieldOptions
from .quick_sight_pivot_table_field_wells import QuickSightPivotTableFieldWells
from .quick_sight_pivot_table_options import QuickSightPivotTableOptions
from .quick_sight_pivot_table_paginated_report_options import QuickSightPivotTablePaginatedReportOptions
from .quick_sight_pivot_table_sort_configuration import QuickSightPivotTableSortConfiguration
from .quick_sight_pivot_table_total_options import QuickSightPivotTableTotalOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightPivotTableConfiguration(BaseModel):
    FieldWells: QuickSightPivotTableFieldWells | None = None
    SortConfiguration: QuickSightPivotTableSortConfiguration | None = None
    TableOptions: QuickSightPivotTableOptions | None = None
    TotalOptions: QuickSightPivotTableTotalOptions | None = None
    FieldOptions: QuickSightPivotTableFieldOptions | None = None
    PaginatedReportOptions: QuickSightPivotTablePaginatedReportOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    DashboardCustomizationVisualOptions: QuickSightDashboardCustomizationVisualOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
