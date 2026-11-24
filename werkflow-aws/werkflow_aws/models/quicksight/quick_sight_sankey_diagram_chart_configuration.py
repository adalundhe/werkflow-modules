from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_sankey_diagram_field_wells import QuickSightSankeyDiagramFieldWells
from .quick_sight_sankey_diagram_sort_configuration import QuickSightSankeyDiagramSortConfiguration
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightSankeyDiagramChartConfiguration(BaseModel):
    FieldWells: QuickSightSankeyDiagramFieldWells | None = None
    SortConfiguration: QuickSightSankeyDiagramSortConfiguration | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
