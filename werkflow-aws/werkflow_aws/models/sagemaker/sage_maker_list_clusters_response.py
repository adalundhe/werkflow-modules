from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_summary import SageMakerClusterSummary


class SageMakerListClustersResponse(BaseModel):
    NextToken: StrictStr | None = None
    ClusterSummaries: list[SageMakerClusterSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
