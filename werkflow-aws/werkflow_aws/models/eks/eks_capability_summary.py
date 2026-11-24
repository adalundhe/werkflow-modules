from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSCapabilitySummary(BaseModel):
    capabilityName: StrictStr | None = None
    arn: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    version: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    modifiedAt: datetime.datetime | StrictStr | None = None
