from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_third_party_job_data import CodePipelineThirdPartyJobData


class CodePipelineThirdPartyJobDetails(BaseModel):
    id: StrictStr | None = None
    data: CodePipelineThirdPartyJobData | None = None
    nonce: StrictStr | None = None
