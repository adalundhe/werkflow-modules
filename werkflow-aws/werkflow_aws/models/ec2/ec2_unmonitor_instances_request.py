from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2UnmonitorInstancesRequest(BaseModel):
    InstanceIds: list[StrictStr]
    MetricCategoryIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
