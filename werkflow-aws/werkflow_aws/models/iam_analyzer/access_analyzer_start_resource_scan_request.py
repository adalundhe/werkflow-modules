from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerStartResourceScanRequest(BaseModel):
    analyzerArn: StrictStr
    resourceArn: StrictStr
    resourceOwnerAccount: StrictStr | None = None
