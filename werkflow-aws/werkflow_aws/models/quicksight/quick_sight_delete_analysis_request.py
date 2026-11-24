from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class QuickSightDeleteAnalysisRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
    RecoveryWindowInDays: StrictInt | None = None
    ForceDeleteWithoutRecovery: StrictBool | None = None
