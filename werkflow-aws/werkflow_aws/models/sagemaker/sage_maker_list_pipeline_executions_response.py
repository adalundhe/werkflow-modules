from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_pipeline_execution_summary import SageMakerPipelineExecutionSummary


class SageMakerListPipelineExecutionsResponse(BaseModel):
    PipelineExecutionSummaries: list[SageMakerPipelineExecutionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
