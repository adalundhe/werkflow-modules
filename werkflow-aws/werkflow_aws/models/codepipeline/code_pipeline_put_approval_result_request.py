from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_approval_result import CodePipelineApprovalResult


class CodePipelinePutApprovalResultRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    actionName: StrictStr
    result: CodePipelineApprovalResult
    token: StrictStr
