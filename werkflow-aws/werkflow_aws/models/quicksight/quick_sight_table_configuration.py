from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dashboard_customization_visual_options import QuickSightDashboardCustomizationVisualOptions
from .quick_sight_table_field_options import QuickSightTableFieldOptions
from .quick_sight_table_field_wells import QuickSightTableFieldWells
from .quick_sight_table_inline_visualization import QuickSightTableInlineVisualization
from .quick_sight_table_options import QuickSightTableOptions
from .quick_sight_table_paginated_report_options import QuickSightTablePaginatedReportOptions
from .quick_sight_table_sort_configuration import QuickSightTableSortConfiguration
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_total_options import QuickSightTotalOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightTableConfiguration(BaseModel):
    FieldWells: QuickSightTableFieldWells | None = None
    SortConfiguration: QuickSightTableSortConfiguration | None = None
    TableOptions: QuickSightTableOptions | None = None
    TotalOptions: QuickSightTotalOptions | None = None
    FieldOptions: QuickSightTableFieldOptions | None = None
    PaginatedReportOptions: QuickSightTablePaginatedReportOptions | None = None
    TableInlineVisualizations: list[QuickSightTableInlineVisualization] | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    DashboardCustomizationVisualOptions: QuickSightDashboardCustomizationVisualOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
