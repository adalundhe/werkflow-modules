from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_action_configuration_property import CodePipelineActionConfigurationProperty
from .code_pipeline_action_type_id import CodePipelineActionTypeId
from .code_pipeline_action_type_settings import CodePipelineActionTypeSettings
from .code_pipeline_artifact_details import CodePipelineArtifactDetails


class CodePipelineActionType(BaseModel):
    id: CodePipelineActionTypeId | None = None
    settings: CodePipelineActionTypeSettings | None = None
    actionConfigurationProperties: list[CodePipelineActionConfigurationProperty] | None = None
    inputArtifactDetails: CodePipelineArtifactDetails | None = None
    outputArtifactDetails: CodePipelineArtifactDetails | None = None
