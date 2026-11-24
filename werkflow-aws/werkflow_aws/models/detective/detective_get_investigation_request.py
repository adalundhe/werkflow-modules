from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveGetInvestigationRequest(BaseModel):
    GraphArn: StrictStr
    InvestigationId: StrictStr
