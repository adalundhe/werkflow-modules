from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_contribution_analysis_default import QuickSightContributionAnalysisDefault
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_donut_options import QuickSightDonutOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_pie_chart_field_wells import QuickSightPieChartFieldWells
from .quick_sight_pie_chart_sort_configuration import QuickSightPieChartSortConfiguration
from .quick_sight_small_multiples_options import QuickSightSmallMultiplesOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightPieChartConfiguration(BaseModel):
    FieldWells: QuickSightPieChartFieldWells | None = None
    SortConfiguration: QuickSightPieChartSortConfiguration | None = None
    DonutOptions: QuickSightDonutOptions | None = None
    SmallMultiplesOptions: QuickSightSmallMultiplesOptions | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ValueLabelOptions: QuickSightChartAxisLabelOptions | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    ContributionAnalysisDefaults: list[QuickSightContributionAnalysisDefault] | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
