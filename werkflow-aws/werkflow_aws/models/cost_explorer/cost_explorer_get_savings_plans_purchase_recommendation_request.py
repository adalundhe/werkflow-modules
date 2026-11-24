from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression


class CostExplorerGetSavingsPlansPurchaseRecommendationRequest(BaseModel):
    SavingsPlansType: Literal['COMPUTE_SP', 'EC2_INSTANCE_SP', 'SAGEMAKER_SP', 'DATABASE_SP']
    TermInYears: Literal['ONE_YEAR', 'THREE_YEARS']
    PaymentOption: Literal['NO_UPFRONT', 'PARTIAL_UPFRONT', 'ALL_UPFRONT', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'HEAVY_UTILIZATION']
    LookbackPeriodInDays: Literal['SEVEN_DAYS', 'THIRTY_DAYS', 'SIXTY_DAYS']
    AccountScope: Literal['PAYER', 'LINKED'] | None = None
    NextPageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
    Filter: CostExplorerExpression | None = None
