from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraScoreAttributes(BaseModel):
    ScoreConfidence: StrictStr | None = None
