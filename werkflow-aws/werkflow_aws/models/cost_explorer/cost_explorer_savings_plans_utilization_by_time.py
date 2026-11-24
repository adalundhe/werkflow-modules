from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_savings_plans_amortized_commitment import CostExplorerSavingsPlansAmortizedCommitment
from .cost_explorer_savings_plans_savings import CostExplorerSavingsPlansSavings
from .cost_explorer_savings_plans_utilization import CostExplorerSavingsPlansUtilization


class CostExplorerSavingsPlansUtilizationByTime(BaseModel):
    TimePeriod: CostExplorerDateInterval | None = None
    Utilization: CostExplorerSavingsPlansUtilization | None = None
    Savings: CostExplorerSavingsPlansSavings | None = None
    AmortizedCommitment: CostExplorerSavingsPlansAmortizedCommitment | None = None
