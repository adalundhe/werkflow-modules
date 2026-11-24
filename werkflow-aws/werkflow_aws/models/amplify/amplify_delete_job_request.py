from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteJobRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobId: StrictStr
