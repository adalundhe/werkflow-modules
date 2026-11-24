from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_action_execution_input import CodePipelineActionExecutionInput
from .code_pipeline_action_execution_output import CodePipelineActionExecutionOutput


class CodePipelineActionExecutionDetail(BaseModel):
    pipelineExecutionId: StrictStr | None = None
    actionExecutionId: StrictStr | None = None
    pipelineVersion: StrictInt | None = None
    stageName: StrictStr | None = None
    actionName: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    lastUpdateTime: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    status: StrictStr | None = None
    input: CodePipelineActionExecutionInput | None = None
    output: CodePipelineActionExecutionOutput | None = None
