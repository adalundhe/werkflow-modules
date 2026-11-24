from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyStopJobRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobId: StrictStr
