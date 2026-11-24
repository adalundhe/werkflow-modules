from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessScoreAttributes(BaseModel):
    scoreConfidence: StrictStr | None = None
