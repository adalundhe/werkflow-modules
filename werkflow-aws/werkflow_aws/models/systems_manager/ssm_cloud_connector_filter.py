from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMCloudConnectorFilter(BaseModel):
    FilterKey: Literal['SubscriptionId', 'TenantId', 'ProjectId', 'OrganizationId'] | None = None
    FilterValues: list[StrictStr] | None = None
