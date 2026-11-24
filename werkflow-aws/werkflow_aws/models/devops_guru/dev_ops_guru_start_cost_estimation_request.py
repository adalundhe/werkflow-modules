from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_cost_estimation_resource_collection_filter import DevOpsGuruCostEstimationResourceCollectionFilter


class DevOpsGuruStartCostEstimationRequest(BaseModel):
    ResourceCollection: DevOpsGuruCostEstimationResourceCollectionFilter
    ClientToken: StrictStr | None = None
