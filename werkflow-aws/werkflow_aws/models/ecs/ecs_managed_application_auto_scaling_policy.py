from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ECSManagedApplicationAutoScalingPolicy(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    policyType: StrictStr | None = None
    targetValue: StrictFloat | StrictInt | None = None
    metric: StrictStr | None = None
