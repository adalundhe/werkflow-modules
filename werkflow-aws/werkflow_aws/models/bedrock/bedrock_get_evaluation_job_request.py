from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetEvaluationJobRequest(BaseModel):
    jobIdentifier: StrictStr
