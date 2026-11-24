from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_failure_details import CodePipelineFailureDetails


class CodePipelinePutJobFailureResultRequest(BaseModel):
    jobId: StrictStr
    failureDetails: CodePipelineFailureDetails
