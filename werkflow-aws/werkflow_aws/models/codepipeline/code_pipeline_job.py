from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_job_data import CodePipelineJobData


class CodePipelineJob(BaseModel):
    id: StrictStr | None = None
    data: CodePipelineJobData | None = None
    nonce: StrictStr | None = None
    accountId: StrictStr | None = None
