from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerGetFindingsStatisticsRequest(BaseModel):
    analyzerArn: StrictStr
