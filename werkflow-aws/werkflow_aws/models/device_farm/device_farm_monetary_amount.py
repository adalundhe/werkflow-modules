from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DeviceFarmMonetaryAmount(BaseModel):
    amount: StrictFloat | StrictInt | None = None
    currencyCode: StrictStr | None = None
