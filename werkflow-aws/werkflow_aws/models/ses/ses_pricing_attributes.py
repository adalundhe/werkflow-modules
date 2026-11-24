from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESPricingAttributes(BaseModel):
    CurrentPlan: StrictStr | None = None
    NextPlan: StrictStr | None = None
