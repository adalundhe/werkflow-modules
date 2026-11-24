from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class OpenSearchTrafficSplitRequestOptions(BaseModel):
    Strategy: Literal['ShiftReadTrafficPercent']
    CloneReadTrafficPercent: StrictInt
