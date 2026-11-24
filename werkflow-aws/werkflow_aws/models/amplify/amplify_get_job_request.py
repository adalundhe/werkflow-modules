from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetJobRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobId: StrictStr
