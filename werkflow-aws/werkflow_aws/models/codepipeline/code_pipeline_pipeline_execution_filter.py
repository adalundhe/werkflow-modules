from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_succeeded_in_stage_filter import CodePipelineSucceededInStageFilter


class CodePipelinePipelineExecutionFilter(BaseModel):
    succeededInStage: CodePipelineSucceededInStageFilter | None = None
