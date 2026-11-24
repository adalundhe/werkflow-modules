from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_savings_plans_amortized_commitment import CostExplorerSavingsPlansAmortizedCommitment
from .cost_explorer_savings_plans_savings import CostExplorerSavingsPlansSavings
from .cost_explorer_savings_plans_utilization import CostExplorerSavingsPlansUtilization


class CostExplorerSavingsPlansUtilizationDetail(BaseModel):
    SavingsPlanArn: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    Utilization: CostExplorerSavingsPlansUtilization | None = None
    Savings: CostExplorerSavingsPlansSavings | None = None
    AmortizedCommitment: CostExplorerSavingsPlansAmortizedCommitment | None = None
