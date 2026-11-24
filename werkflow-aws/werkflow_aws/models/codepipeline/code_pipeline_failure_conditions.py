from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_condition import CodePipelineCondition
from .code_pipeline_retry_configuration import CodePipelineRetryConfiguration


class CodePipelineFailureConditions(BaseModel):
    result: StrictStr | None = None
    retryConfiguration: CodePipelineRetryConfiguration | None = None
    conditions: list[CodePipelineCondition] | None = None
