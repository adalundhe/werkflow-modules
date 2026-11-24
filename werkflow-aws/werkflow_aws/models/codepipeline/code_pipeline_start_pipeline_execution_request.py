from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_pipeline_variable import CodePipelinePipelineVariable
from .code_pipeline_source_revision_override import CodePipelineSourceRevisionOverride


class CodePipelineStartPipelineExecutionRequest(BaseModel):
    name: StrictStr
    variables: list[CodePipelinePipelineVariable] | None = None
    clientRequestToken: StrictStr | None = None
    sourceRevisions: list[CodePipelineSourceRevisionOverride] | None = None
