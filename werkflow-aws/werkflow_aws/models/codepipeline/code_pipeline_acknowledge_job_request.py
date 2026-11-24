from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineAcknowledgeJobRequest(BaseModel):
    jobId: StrictStr
    nonce: StrictStr
