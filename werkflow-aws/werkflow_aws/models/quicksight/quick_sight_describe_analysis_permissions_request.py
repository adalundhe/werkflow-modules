from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAnalysisPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
