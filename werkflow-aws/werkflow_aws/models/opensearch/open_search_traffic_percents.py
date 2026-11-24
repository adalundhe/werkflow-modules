from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchTrafficPercents(BaseModel):
    PrimaryReadTrafficPercent: StrictInt | None = None
    CloneReadTrafficPercent: StrictInt | None = None
