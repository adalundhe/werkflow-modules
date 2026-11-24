from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_pipeline_version_summary import SageMakerPipelineVersionSummary


class SageMakerListPipelineVersionsResponse(BaseModel):
    PipelineVersionSummaries: list[SageMakerPipelineVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
