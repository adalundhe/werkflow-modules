from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchInsightTimeRange(BaseModel):
    From: StrictInt
    To: StrictInt
