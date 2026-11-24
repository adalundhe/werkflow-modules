from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dev_ops_guru_cost_estimation_resource_collection_filter import DevOpsGuruCostEstimationResourceCollectionFilter
from .dev_ops_guru_cost_estimation_time_range import DevOpsGuruCostEstimationTimeRange
from .dev_ops_guru_service_resource_cost import DevOpsGuruServiceResourceCost


class DevOpsGuruGetCostEstimationResponse(BaseModel):
    ResourceCollection: DevOpsGuruCostEstimationResourceCollectionFilter | None = None
    Status: StrictStr | None = None
    Costs: list[DevOpsGuruServiceResourceCost] | None = None
    TimeRange: DevOpsGuruCostEstimationTimeRange | None = None
    TotalCost: StrictFloat | StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
