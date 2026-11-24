from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ResilienceHubCost(BaseModel):
    amount: StrictFloat | StrictInt | None = None
    currency: StrictStr | None = None
    frequency: StrictStr | None = None
