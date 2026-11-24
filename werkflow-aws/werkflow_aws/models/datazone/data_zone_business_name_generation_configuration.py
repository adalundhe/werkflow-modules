from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneBusinessNameGenerationConfiguration(BaseModel):
    enabled: StrictBool | None = None
