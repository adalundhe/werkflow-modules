from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_histogram_aggregated_field_wells import QuickSightHistogramAggregatedFieldWells


class QuickSightHistogramFieldWells(BaseModel):
    HistogramAggregatedFieldWells: QuickSightHistogramAggregatedFieldWells | None = None
