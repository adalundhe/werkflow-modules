from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_current_revision import CodePipelineCurrentRevision
from .code_pipeline_execution_details import CodePipelineExecutionDetails


class CodePipelinePutThirdPartyJobSuccessResultRequest(BaseModel):
    jobId: StrictStr
    clientToken: StrictStr
    currentRevision: CodePipelineCurrentRevision | None = None
    continuationToken: StrictStr | None = None
    executionDetails: CodePipelineExecutionDetails | None = None
