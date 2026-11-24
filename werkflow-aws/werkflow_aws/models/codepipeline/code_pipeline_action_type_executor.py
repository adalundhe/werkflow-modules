from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_executor_configuration import CodePipelineExecutorConfiguration


class CodePipelineActionTypeExecutor(BaseModel):
    configuration: CodePipelineExecutorConfiguration | None = None
    type: StrictStr | None = None
    policyStatementsTemplate: StrictStr | None = None
    jobTimeout: StrictInt | None = None
