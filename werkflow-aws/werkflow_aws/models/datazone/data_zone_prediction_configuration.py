from __future__ import annotations
from pydantic import BaseModel
from .data_zone_business_name_generation_configuration import DataZoneBusinessNameGenerationConfiguration


class DataZonePredictionConfiguration(BaseModel):
    businessNameGeneration: DataZoneBusinessNameGenerationConfiguration | None = None
