from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSManagedInstancesNetworkConfiguration(BaseModel):
    subnets: list[StrictStr] | None = None
    securityGroups: list[StrictStr] | None = None
