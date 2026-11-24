from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2RevenueBreakdown(BaseModel):
    TotalAmount: StrictStr | None = None
    VerifiedAmount: StrictStr | None = None
    UnverifiedAmount: StrictStr | None = None
    Currency: StrictStr | None = None
    TotalSettled: StrictInt | None = None
    TotalMonetizeServed: StrictInt | None = None
