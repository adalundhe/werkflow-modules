from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_savings_plans import CostExplorerSavingsPlans


class CostExplorerSavingsPlansPurchaseAnalysisConfiguration(BaseModel):
    AccountScope: StrictStr | None = None
    AccountId: StrictStr | None = None
    AnalysisType: StrictStr | None = None
    SavingsPlansToAdd: list[CostExplorerSavingsPlans] | None = None
    SavingsPlansToExclude: list[StrictStr] | None = None
    LookBackTimePeriod: CostExplorerDateInterval | None = None
    SavingsPlansTargetCoverage: StrictInt | None = None
