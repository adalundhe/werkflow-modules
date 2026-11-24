from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeCompilationJobRequest(BaseModel):
    CompilationJobName: StrictStr
