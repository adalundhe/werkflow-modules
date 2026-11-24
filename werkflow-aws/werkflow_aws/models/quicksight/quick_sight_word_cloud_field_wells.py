from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_word_cloud_aggregated_field_wells import QuickSightWordCloudAggregatedFieldWells


class QuickSightWordCloudFieldWells(BaseModel):
    WordCloudAggregatedFieldWells: QuickSightWordCloudAggregatedFieldWells | None = None
