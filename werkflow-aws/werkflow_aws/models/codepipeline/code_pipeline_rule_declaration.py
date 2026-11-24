from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_input_artifact import CodePipelineInputArtifact
from .code_pipeline_rule_type_id import CodePipelineRuleTypeId


class CodePipelineRuleDeclaration(BaseModel):
    name: StrictStr | None = None
    ruleTypeId: CodePipelineRuleTypeId | None = None
    configuration: dict[StrictStr, StrictStr] | None = None
    commands: list[StrictStr] | None = None
    inputArtifacts: list[CodePipelineInputArtifact] | None = None
    roleArn: StrictStr | None = None
    region: StrictStr | None = None
    timeoutInMinutes: StrictInt | None = None
