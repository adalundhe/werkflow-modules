from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_operation_summary import SageMakerClusterOperationSummary


class SageMakerListClusterOperationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ClusterOperationSummaries: list[SageMakerClusterOperationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
