from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockBatchDeleteEvaluationJobRequest(BaseModel):
    jobIdentifiers: list[StrictStr]
