from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockBatchDeleteEvaluationJobItem(BaseModel):
    jobIdentifier: StrictStr | None = None
    jobStatus: StrictStr | None = None
