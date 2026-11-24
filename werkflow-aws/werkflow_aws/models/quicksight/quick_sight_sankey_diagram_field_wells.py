from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_sankey_diagram_aggregated_field_wells import QuickSightSankeyDiagramAggregatedFieldWells


class QuickSightSankeyDiagramFieldWells(BaseModel):
    SankeyDiagramAggregatedFieldWells: QuickSightSankeyDiagramAggregatedFieldWells | None = None
