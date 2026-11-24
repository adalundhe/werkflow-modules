from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteCompilationJobRequest(BaseModel):
    CompilationJobName: StrictStr
