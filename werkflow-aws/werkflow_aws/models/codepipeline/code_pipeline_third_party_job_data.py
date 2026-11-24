from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_aws_session_credentials import CodePipelineAWSSessionCredentials
from .code_pipeline_action_configuration import CodePipelineActionConfiguration
from .code_pipeline_action_type_id import CodePipelineActionTypeId
from .code_pipeline_artifact import CodePipelineArtifact
from .code_pipeline_encryption_key import CodePipelineEncryptionKey
from .code_pipeline_pipeline_context import CodePipelinePipelineContext


class CodePipelineThirdPartyJobData(BaseModel):
    actionTypeId: CodePipelineActionTypeId | None = None
    actionConfiguration: CodePipelineActionConfiguration | None = None
    pipelineContext: CodePipelinePipelineContext | None = None
    inputArtifacts: list[CodePipelineArtifact] | None = None
    outputArtifacts: list[CodePipelineArtifact] | None = None
    artifactCredentials: CodePipelineAWSSessionCredentials | None = None
    continuationToken: StrictStr | None = None
    encryptionKey: CodePipelineEncryptionKey | None = None
