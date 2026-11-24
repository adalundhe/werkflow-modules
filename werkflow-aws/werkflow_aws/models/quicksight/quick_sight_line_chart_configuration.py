from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_contribution_analysis_default import QuickSightContributionAnalysisDefault
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_forecast_configuration import QuickSightForecastConfiguration
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_line_chart_default_series_settings import QuickSightLineChartDefaultSeriesSettings
from .quick_sight_line_chart_field_wells import QuickSightLineChartFieldWells
from .quick_sight_line_chart_sort_configuration import QuickSightLineChartSortConfiguration
from .quick_sight_line_series_axis_display_options import QuickSightLineSeriesAxisDisplayOptions
from .quick_sight_reference_line import QuickSightReferenceLine
from .quick_sight_series_item import QuickSightSeriesItem
from .quick_sight_single_axis_options import QuickSightSingleAxisOptions
from .quick_sight_small_multiples_options import QuickSightSmallMultiplesOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightLineChartConfiguration(BaseModel):
    FieldWells: QuickSightLineChartFieldWells | None = None
    SortConfiguration: QuickSightLineChartSortConfiguration | None = None
    ForecastConfigurations: list[QuickSightForecastConfiguration] | None = None
    Type: StrictStr | None = None
    SmallMultiplesOptions: QuickSightSmallMultiplesOptions | None = None
    XAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    XAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    PrimaryYAxisDisplayOptions: QuickSightLineSeriesAxisDisplayOptions | None = None
    PrimaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    SecondaryYAxisDisplayOptions: QuickSightLineSeriesAxisDisplayOptions | None = None
    SecondaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    SingleAxisOptions: QuickSightSingleAxisOptions | None = None
    DefaultSeriesSettings: QuickSightLineChartDefaultSeriesSettings | None = None
    Series: list[QuickSightSeriesItem] | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    ReferenceLines: list[QuickSightReferenceLine] | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    ContributionAnalysisDefaults: list[QuickSightContributionAnalysisDefault] | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
