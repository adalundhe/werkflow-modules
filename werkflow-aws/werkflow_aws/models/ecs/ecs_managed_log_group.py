from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSManagedLogGroup(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    logGroupName: StrictStr | None = None
