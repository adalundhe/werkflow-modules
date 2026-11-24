from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSManagedLoadBalancer(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    scheme: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
