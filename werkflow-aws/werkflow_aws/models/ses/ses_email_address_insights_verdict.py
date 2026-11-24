from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESEmailAddressInsightsVerdict(BaseModel):
    ConfidenceVerdict: StrictStr | None = None
