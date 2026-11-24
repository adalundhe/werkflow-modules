from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_pipeline_execution_trigger import CodePipelineExecutionTrigger
from .code_pipeline_pipeline_rollback_metadata import CodePipelinePipelineRollbackMetadata
from .code_pipeline_source_revision import CodePipelineSourceRevision
from .code_pipeline_stop_execution_trigger import CodePipelineStopExecutionTrigger


class CodePipelinePipelineExecutionSummary(BaseModel):
    pipelineExecutionId: StrictStr | None = None
    status: StrictStr | None = None
    statusSummary: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    lastUpdateTime: datetime.datetime | StrictStr | None = None
    sourceRevisions: list[CodePipelineSourceRevision] | None = None
    trigger: CodePipelineExecutionTrigger | None = None
    stopTrigger: CodePipelineStopExecutionTrigger | None = None
    executionMode: StrictStr | None = None
    executionType: StrictStr | None = None
    rollbackMetadata: CodePipelinePipelineRollbackMetadata | None = None
