from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EksAnywhereSubscriptionTerm(BaseModel):
    duration: StrictInt | None = None
    unit: StrictStr | None = None
