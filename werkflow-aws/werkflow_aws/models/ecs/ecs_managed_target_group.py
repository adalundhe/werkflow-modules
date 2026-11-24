from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ECSManagedTargetGroup(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    healthCheckPath: StrictStr | None = None
    healthCheckPort: StrictInt | None = None
    port: StrictInt | None = None
