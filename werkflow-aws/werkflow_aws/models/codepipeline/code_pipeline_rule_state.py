from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_rule_execution import CodePipelineRuleExecution
from .code_pipeline_rule_revision import CodePipelineRuleRevision


class CodePipelineRuleState(BaseModel):
    ruleName: StrictStr | None = None
    currentRevision: CodePipelineRuleRevision | None = None
    latestExecution: CodePipelineRuleExecution | None = None
    entityUrl: StrictStr | None = None
    revisionUrl: StrictStr | None = None
