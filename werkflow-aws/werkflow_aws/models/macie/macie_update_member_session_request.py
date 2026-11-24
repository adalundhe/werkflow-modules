from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieUpdateMemberSessionRequest(BaseModel):
    id: StrictStr
    status: Literal['PAUSED', 'ENABLED']
