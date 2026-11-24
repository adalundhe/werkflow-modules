from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_artifact_store import CodePipelineArtifactStore
from .code_pipeline_pipeline_trigger_declaration import CodePipelinePipelineTriggerDeclaration
from .code_pipeline_pipeline_variable_declaration import CodePipelinePipelineVariableDeclaration
from .code_pipeline_stage_declaration import CodePipelineStageDeclaration


class CodePipelinePipelineDeclaration(BaseModel):
    name: StrictStr | None = None
    roleArn: StrictStr | None = None
    artifactStore: CodePipelineArtifactStore | None = None
    artifactStores: dict[StrictStr, CodePipelineArtifactStore] | None = None
    stages: list[CodePipelineStageDeclaration] | None = None
    version: StrictInt | None = None
    executionMode: StrictStr | None = None
    pipelineType: StrictStr | None = None
    variables: list[CodePipelinePipelineVariableDeclaration] | None = None
    triggers: list[CodePipelinePipelineTriggerDeclaration] | None = None
