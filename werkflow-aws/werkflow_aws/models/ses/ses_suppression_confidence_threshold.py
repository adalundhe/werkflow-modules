from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSuppressionConfidenceThreshold(BaseModel):
    ConfidenceVerdictThreshold: StrictStr | None = None
