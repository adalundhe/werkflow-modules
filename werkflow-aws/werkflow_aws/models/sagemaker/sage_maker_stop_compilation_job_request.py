from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopCompilationJobRequest(BaseModel):
    CompilationJobName: StrictStr
