from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .code_pipeline_action_type_id import CodePipelineActionTypeId


class CodePipelinePollForThirdPartyJobsRequest(BaseModel):
    actionTypeId: CodePipelineActionTypeId
    maxBatchSize: StrictInt | None = None
