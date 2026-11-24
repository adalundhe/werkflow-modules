from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CostExplorerSavingsPlans(BaseModel):
    PaymentOption: StrictStr | None = None
    SavingsPlansType: StrictStr | None = None
    Region: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    TermInYears: StrictStr | None = None
    SavingsPlansCommitment: StrictFloat | StrictInt | None = None
    OfferingId: StrictStr | None = None
