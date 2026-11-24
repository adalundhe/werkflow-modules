from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_savings_plans_coverage_data import CostExplorerSavingsPlansCoverageData


class CostExplorerSavingsPlansCoverage(BaseModel):
    Attributes: dict[StrictStr, StrictStr] | None = None
    Coverage: CostExplorerSavingsPlansCoverageData | None = None
    TimePeriod: CostExplorerDateInterval | None = None
