from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_word_cloud_field_wells import QuickSightWordCloudFieldWells
from .quick_sight_word_cloud_options import QuickSightWordCloudOptions
from .quick_sight_word_cloud_sort_configuration import QuickSightWordCloudSortConfiguration


class QuickSightWordCloudChartConfiguration(BaseModel):
    FieldWells: QuickSightWordCloudFieldWells | None = None
    SortConfiguration: QuickSightWordCloudSortConfiguration | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    WordCloudOptions: QuickSightWordCloudOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
