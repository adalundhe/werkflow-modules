from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_rule_execution_input import CodePipelineRuleExecutionInput
from .code_pipeline_rule_execution_output import CodePipelineRuleExecutionOutput


class CodePipelineRuleExecutionDetail(BaseModel):
    pipelineExecutionId: StrictStr | None = None
    ruleExecutionId: StrictStr | None = None
    pipelineVersion: StrictInt | None = None
    stageName: StrictStr | None = None
    ruleName: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    lastUpdateTime: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    status: StrictStr | None = None
    input: CodePipelineRuleExecutionInput | None = None
    output: CodePipelineRuleExecutionOutput | None = None
