from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientSoftwareSetSummary(BaseModel):
    id: StrictStr | None = None
    version: StrictStr | None = None
    releasedAt: datetime.datetime | StrictStr | None = None
    supportedUntil: datetime.datetime | StrictStr | None = None
    validationStatus: StrictStr | None = None
    arn: StrictStr | None = None
