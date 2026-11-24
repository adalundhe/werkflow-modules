from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetModelCopyJobRequest(BaseModel):
    jobArn: StrictStr
