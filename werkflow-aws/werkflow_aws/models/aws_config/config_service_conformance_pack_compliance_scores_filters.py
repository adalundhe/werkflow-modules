from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackComplianceScoresFilters(BaseModel):
    ConformancePackNames: list[StrictStr]
