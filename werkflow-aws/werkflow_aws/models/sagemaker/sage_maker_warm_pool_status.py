from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_warm_pool_resource_status import SageMakerWarmPoolResourceStatus


class SageMakerWarmPoolStatus(BaseModel):
    Status: SageMakerWarmPoolResourceStatus | None = None
    ResourceRetainedBillableTimeInSeconds: StrictInt | None = None
    ReusedByJob: StrictStr | None = None
