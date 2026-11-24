from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockBatchDeleteEvaluationJobError(BaseModel):
    jobIdentifier: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
