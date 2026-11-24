from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_artifact_details import CodePipelineArtifactDetails
from .code_pipeline_rule_configuration_property import CodePipelineRuleConfigurationProperty
from .code_pipeline_rule_type_id import CodePipelineRuleTypeId
from .code_pipeline_rule_type_settings import CodePipelineRuleTypeSettings


class CodePipelineRuleType(BaseModel):
    id: CodePipelineRuleTypeId | None = None
    settings: CodePipelineRuleTypeSettings | None = None
    ruleConfigurationProperties: list[CodePipelineRuleConfigurationProperty] | None = None
    inputArtifactDetails: CodePipelineArtifactDetails | None = None
