from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_artifact_revision import CodePipelineArtifactRevision
from .code_pipeline_execution_trigger import CodePipelineExecutionTrigger
from .code_pipeline_pipeline_rollback_metadata import CodePipelinePipelineRollbackMetadata
from .code_pipeline_resolved_pipeline_variable import CodePipelineResolvedPipelineVariable


class CodePipelinePipelineExecution(BaseModel):
    pipelineName: StrictStr | None = None
    pipelineVersion: StrictInt | None = None
    pipelineExecutionId: StrictStr | None = None
    status: StrictStr | None = None
    statusSummary: StrictStr | None = None
    artifactRevisions: list[CodePipelineArtifactRevision] | None = None
    variables: list[CodePipelineResolvedPipelineVariable] | None = None
    trigger: CodePipelineExecutionTrigger | None = None
    executionMode: StrictStr | None = None
    executionType: StrictStr | None = None
    rollbackMetadata: CodePipelinePipelineRollbackMetadata | None = None
