from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractGetLendingAnalysisSummaryRequest(BaseModel):
    JobId: StrictStr
