from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_savings_plans_coverage import CostExplorerSavingsPlansCoverage


class CostExplorerGetSavingsPlansCoverageResponse(BaseModel):
    SavingsPlansCoverages: list[CostExplorerSavingsPlansCoverage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
