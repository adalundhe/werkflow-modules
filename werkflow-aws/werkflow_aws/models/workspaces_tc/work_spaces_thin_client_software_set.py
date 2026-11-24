from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_thin_client_software import WorkSpacesThinClientSoftware


class WorkSpacesThinClientSoftwareSet(BaseModel):
    id: StrictStr | None = None
    version: StrictStr | None = None
    releasedAt: datetime.datetime | StrictStr | None = None
    supportedUntil: datetime.datetime | StrictStr | None = None
    validationStatus: StrictStr | None = None
    software: list[WorkSpacesThinClientSoftware] | None = None
    arn: StrictStr | None = None
