from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_combo_chart_default_series_settings import QuickSightComboChartDefaultSeriesSettings
from .quick_sight_combo_chart_field_wells import QuickSightComboChartFieldWells
from .quick_sight_combo_chart_sort_configuration import QuickSightComboChartSortConfiguration
from .quick_sight_combo_series_item import QuickSightComboSeriesItem
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_reference_line import QuickSightReferenceLine
from .quick_sight_single_axis_options import QuickSightSingleAxisOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightComboChartConfiguration(BaseModel):
    FieldWells: QuickSightComboChartFieldWells | None = None
    SortConfiguration: QuickSightComboChartSortConfiguration | None = None
    BarsArrangement: StrictStr | None = None
    CategoryAxis: QuickSightAxisDisplayOptions | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    PrimaryYAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    PrimaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    SecondaryYAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    SecondaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    SingleAxisOptions: QuickSightSingleAxisOptions | None = None
    ColorLabelOptions: QuickSightChartAxisLabelOptions | None = None
    DefaultSeriesSettings: QuickSightComboChartDefaultSeriesSettings | None = None
    Series: list[QuickSightComboSeriesItem] | None = None
    Legend: QuickSightLegendOptions | None = None
    BarDataLabels: QuickSightDataLabelOptions | None = None
    LineDataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    ReferenceLines: list[QuickSightReferenceLine] | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
