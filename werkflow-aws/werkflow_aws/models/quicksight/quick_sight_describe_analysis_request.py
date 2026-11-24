from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAnalysisRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
