from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_histogram_bin_options import QuickSightHistogramBinOptions
from .quick_sight_histogram_field_wells import QuickSightHistogramFieldWells
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightHistogramConfiguration(BaseModel):
    FieldWells: QuickSightHistogramFieldWells | None = None
    XAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    XAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    YAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    BinOptions: QuickSightHistogramBinOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
