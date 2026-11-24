from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_artifact_detail import CodePipelineArtifactDetail
from .code_pipeline_rule_type_id import CodePipelineRuleTypeId


class CodePipelineRuleExecutionInput(BaseModel):
    ruleTypeId: CodePipelineRuleTypeId | None = None
    configuration: dict[StrictStr, StrictStr] | None = None
    resolvedConfiguration: dict[StrictStr, StrictStr] | None = None
    roleArn: StrictStr | None = None
    region: StrictStr | None = None
    inputArtifacts: list[CodePipelineArtifactDetail] | None = None
