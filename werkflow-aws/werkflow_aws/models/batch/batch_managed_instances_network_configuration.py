from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchManagedInstancesNetworkConfiguration(BaseModel):
    subnets: list[StrictStr] | None = None
    securityGroups: list[StrictStr] | None = None
