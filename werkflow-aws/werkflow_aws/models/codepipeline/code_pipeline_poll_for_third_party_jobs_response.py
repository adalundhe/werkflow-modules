from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_third_party_job import CodePipelineThirdPartyJob


class CodePipelinePollForThirdPartyJobsResponse(BaseModel):
    jobs: list[CodePipelineThirdPartyJob] | None = None
    ResponseMetadata: dict[str, Any] | None = None
