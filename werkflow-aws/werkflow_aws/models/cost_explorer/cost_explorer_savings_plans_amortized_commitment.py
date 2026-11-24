from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansAmortizedCommitment(BaseModel):
    AmortizedRecurringCommitment: StrictStr | None = None
    AmortizedUpfrontCommitment: StrictStr | None = None
    TotalAmortizedCommitment: StrictStr | None = None
