from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_job_details import CodePipelineJobDetails


class CodePipelineGetJobDetailsResponse(BaseModel):
    jobDetails: CodePipelineJobDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
