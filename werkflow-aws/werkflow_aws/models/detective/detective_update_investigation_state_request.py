from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DetectiveUpdateInvestigationStateRequest(BaseModel):
    GraphArn: StrictStr
    InvestigationId: StrictStr
    State: Literal['ACTIVE', 'ARCHIVED']
