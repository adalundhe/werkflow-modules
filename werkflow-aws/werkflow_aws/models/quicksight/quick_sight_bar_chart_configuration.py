from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_bar_chart_default_series_settings import QuickSightBarChartDefaultSeriesSettings
from .quick_sight_bar_chart_field_wells import QuickSightBarChartFieldWells
from .quick_sight_bar_chart_sort_configuration import QuickSightBarChartSortConfiguration
from .quick_sight_bar_series_item import QuickSightBarSeriesItem
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_contribution_analysis_default import QuickSightContributionAnalysisDefault
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_reference_line import QuickSightReferenceLine
from .quick_sight_small_multiples_options import QuickSightSmallMultiplesOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightBarChartConfiguration(BaseModel):
    FieldWells: QuickSightBarChartFieldWells | None = None
    SortConfiguration: QuickSightBarChartSortConfiguration | None = None
    Orientation: StrictStr | None = None
    BarsArrangement: StrictStr | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    SmallMultiplesOptions: QuickSightSmallMultiplesOptions | None = None
    CategoryAxis: QuickSightAxisDisplayOptions | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ValueAxis: QuickSightAxisDisplayOptions | None = None
    ValueLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColorLabelOptions: QuickSightChartAxisLabelOptions | None = None
    DefaultSeriesSettings: QuickSightBarChartDefaultSeriesSettings | None = None
    Series: list[QuickSightBarSeriesItem] | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    ReferenceLines: list[QuickSightReferenceLine] | None = None
    ContributionAnalysisDefaults: list[QuickSightContributionAnalysisDefault] | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
