from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_type_artifact_details import CodePipelineActionTypeArtifactDetails
from .code_pipeline_action_type_executor import CodePipelineActionTypeExecutor
from .code_pipeline_action_type_identifier import CodePipelineActionTypeIdentifier
from .code_pipeline_action_type_permissions import CodePipelineActionTypePermissions
from .code_pipeline_action_type_property import CodePipelineActionTypeProperty
from .code_pipeline_action_type_urls import CodePipelineActionTypeUrls


class CodePipelineActionTypeDeclaration(BaseModel):
    description: StrictStr | None = None
    executor: CodePipelineActionTypeExecutor | None = None
    id: CodePipelineActionTypeIdentifier | None = None
    inputArtifactDetails: CodePipelineActionTypeArtifactDetails | None = None
    outputArtifactDetails: CodePipelineActionTypeArtifactDetails | None = None
    permissions: CodePipelineActionTypePermissions | None = None
    properties: list[CodePipelineActionTypeProperty] | None = None
    urls: CodePipelineActionTypeUrls | None = None
