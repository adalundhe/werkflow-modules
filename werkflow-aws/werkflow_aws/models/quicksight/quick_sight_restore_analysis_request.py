from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightRestoreAnalysisRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
    RestoreToFolders: StrictBool | None = None
