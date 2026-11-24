from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_resource_budget_estimate import LightsailResourceBudgetEstimate


class LightsailGetCostEstimateResponse(BaseModel):
    resourcesBudgetEstimate: list[LightsailResourceBudgetEstimate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
