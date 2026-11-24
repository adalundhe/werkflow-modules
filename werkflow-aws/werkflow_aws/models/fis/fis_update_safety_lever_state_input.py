from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FISUpdateSafetyLeverStateInput(BaseModel):
    status: Literal['disengaged', 'engaged']
    reason: StrictStr
