from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneRecommendationConfiguration(BaseModel):
    enableBusinessNameGeneration: StrictBool | None = None
