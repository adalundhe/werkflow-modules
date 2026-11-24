from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ComputeOptimizerRecommendationPreferences(BaseModel):
    cpuVendorArchitectures: list[Literal['AWS_ARM64', 'CURRENT']] | None = None
