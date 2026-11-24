from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ECSManagedScalableTarget(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    minCapacity: StrictInt | None = None
    maxCapacity: StrictInt | None = None
