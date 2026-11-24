from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_execution_result import CodePipelineActionExecutionResult
from .code_pipeline_artifact_detail import CodePipelineArtifactDetail


class CodePipelineActionExecutionOutput(BaseModel):
    outputArtifacts: list[CodePipelineArtifactDetail] | None = None
    executionResult: CodePipelineActionExecutionResult | None = None
    outputVariables: dict[StrictStr, StrictStr] | None = None
