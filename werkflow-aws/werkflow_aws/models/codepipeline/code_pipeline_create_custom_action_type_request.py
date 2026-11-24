from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_configuration_property import CodePipelineActionConfigurationProperty
from .code_pipeline_action_type_settings import CodePipelineActionTypeSettings
from .code_pipeline_artifact_details import CodePipelineArtifactDetails
from .code_pipeline_tag import CodePipelineTag


class CodePipelineCreateCustomActionTypeRequest(BaseModel):
    category: Literal['Source', 'Build', 'Deploy', 'Test', 'Invoke', 'Approval', 'Compute']
    provider: StrictStr
    version: StrictStr
    inputArtifactDetails: CodePipelineArtifactDetails
    outputArtifactDetails: CodePipelineArtifactDetails
    settings: CodePipelineActionTypeSettings | None = None
    configurationProperties: list[CodePipelineActionConfigurationProperty] | None = None
    tags: list[CodePipelineTag] | None = None
