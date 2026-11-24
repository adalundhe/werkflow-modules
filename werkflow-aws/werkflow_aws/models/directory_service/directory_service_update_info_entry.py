from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .directory_service_update_value import DirectoryServiceUpdateValue


class DirectoryServiceUpdateInfoEntry(BaseModel):
    Region: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    InitiatedBy: StrictStr | None = None
    NewValue: DirectoryServiceUpdateValue | None = None
    PreviousValue: DirectoryServiceUpdateValue | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
