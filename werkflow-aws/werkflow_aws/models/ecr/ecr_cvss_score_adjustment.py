from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRCvssScoreAdjustment(BaseModel):
    metric: StrictStr | None = None
    reason: StrictStr | None = None
