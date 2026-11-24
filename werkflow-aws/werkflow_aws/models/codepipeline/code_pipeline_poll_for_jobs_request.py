from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_action_type_id import CodePipelineActionTypeId


class CodePipelinePollForJobsRequest(BaseModel):
    actionTypeId: CodePipelineActionTypeId
    maxBatchSize: StrictInt | None = None
    queryParam: dict[StrictStr, StrictStr] | None = None
