from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesAccountModification(BaseModel):
    ModificationState: StrictStr | None = None
    DedicatedTenancySupport: StrictStr | None = None
    DedicatedTenancyManagementCidrRange: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
