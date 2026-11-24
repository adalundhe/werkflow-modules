from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_job import CodePipelineJob


class CodePipelinePollForJobsResponse(BaseModel):
    jobs: list[CodePipelineJob] | None = None
    ResponseMetadata: dict[str, Any] | None = None
