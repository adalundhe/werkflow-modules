from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_packaging_job_summary import SageMakerEdgePackagingJobSummary


class SageMakerListEdgePackagingJobsResponse(BaseModel):
    EdgePackagingJobSummaries: list[SageMakerEdgePackagingJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
