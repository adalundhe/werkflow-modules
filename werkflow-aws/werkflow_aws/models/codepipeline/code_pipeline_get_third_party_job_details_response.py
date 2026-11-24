from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_third_party_job_details import CodePipelineThirdPartyJobDetails


class CodePipelineGetThirdPartyJobDetailsResponse(BaseModel):
    jobDetails: CodePipelineThirdPartyJobDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
