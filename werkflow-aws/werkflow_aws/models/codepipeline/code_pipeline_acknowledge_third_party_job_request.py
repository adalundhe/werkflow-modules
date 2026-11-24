from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineAcknowledgeThirdPartyJobRequest(BaseModel):
    jobId: StrictStr
    nonce: StrictStr
    clientToken: StrictStr
