from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConfigServiceAggregateConformancePackComplianceCount(BaseModel):
    CompliantConformancePackCount: StrictInt | None = None
    NonCompliantConformancePackCount: StrictInt | None = None
