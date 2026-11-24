from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_radar_chart_field_wells import QuickSightRadarChartFieldWells
from .quick_sight_radar_chart_series_settings import QuickSightRadarChartSeriesSettings
from .quick_sight_radar_chart_sort_configuration import QuickSightRadarChartSortConfiguration
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightRadarChartConfiguration(BaseModel):
    FieldWells: QuickSightRadarChartFieldWells | None = None
    SortConfiguration: QuickSightRadarChartSortConfiguration | None = None
    Shape: StrictStr | None = None
    BaseSeriesSettings: QuickSightRadarChartSeriesSettings | None = None
    StartAngle: StrictFloat | StrictInt | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    AlternateBandColorsVisibility: StrictStr | None = None
    AlternateBandEvenColor: StrictStr | None = None
    AlternateBandOddColor: StrictStr | None = None
    CategoryAxis: QuickSightAxisDisplayOptions | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColorAxis: QuickSightAxisDisplayOptions | None = None
    ColorLabelOptions: QuickSightChartAxisLabelOptions | None = None
    Legend: QuickSightLegendOptions | None = None
    AxesRangeScale: StrictStr | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
