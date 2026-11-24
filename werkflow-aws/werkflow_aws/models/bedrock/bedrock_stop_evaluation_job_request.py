from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockStopEvaluationJobRequest(BaseModel):
    jobIdentifier: StrictStr
