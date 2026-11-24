from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerGetFindingRequest(BaseModel):
    analyzerArn: StrictStr
    id: StrictStr
