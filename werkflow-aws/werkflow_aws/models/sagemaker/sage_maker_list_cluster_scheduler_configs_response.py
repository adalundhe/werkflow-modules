from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_scheduler_config_summary import SageMakerClusterSchedulerConfigSummary


class SageMakerListClusterSchedulerConfigsResponse(BaseModel):
    ClusterSchedulerConfigSummaries: list[SageMakerClusterSchedulerConfigSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
