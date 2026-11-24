from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAnalysisDefinitionRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
