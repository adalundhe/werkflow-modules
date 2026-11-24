from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_compilation_job_summary import SageMakerCompilationJobSummary


class SageMakerListCompilationJobsResponse(BaseModel):
    CompilationJobSummaries: list[SageMakerCompilationJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
