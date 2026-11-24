from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_pipeline_summary import SageMakerPipelineSummary


class SageMakerListPipelinesResponse(BaseModel):
    PipelineSummaries: list[SageMakerPipelineSummary] | None = None
    NextToken: StrictStr | None = None
