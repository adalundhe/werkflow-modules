from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_service_specification import CostExplorerServiceSpecification


class CostExplorerGetReservationPurchaseRecommendationRequest(BaseModel):
    Service: StrictStr
    AccountId: StrictStr | None = None
    Filter: CostExplorerExpression | None = None
    AccountScope: Literal['PAYER', 'LINKED'] | None = None
    LookbackPeriodInDays: Literal['SEVEN_DAYS', 'THIRTY_DAYS', 'SIXTY_DAYS'] | None = None
    TermInYears: Literal['ONE_YEAR', 'THREE_YEARS'] | None = None
    PaymentOption: Literal['NO_UPFRONT', 'PARTIAL_UPFRONT', 'ALL_UPFRONT', 'LIGHT_UTILIZATION', 'MEDIUM_UTILIZATION', 'HEAVY_UTILIZATION'] | None = None
    ServiceSpecification: CostExplorerServiceSpecification | None = None
    PageSize: StrictInt | None = None
    NextPageToken: StrictStr | None = None
