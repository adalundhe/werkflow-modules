from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StepFunctionsBillingDetails(BaseModel):
    billedMemoryUsedInMB: StrictInt | None = None
    billedDurationInMilliseconds: StrictInt | None = None
