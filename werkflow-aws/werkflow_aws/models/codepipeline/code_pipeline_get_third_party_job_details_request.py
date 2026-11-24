from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineGetThirdPartyJobDetailsRequest(BaseModel):
    jobId: StrictStr
    clientToken: StrictStr
