from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .directory_service_hybrid_update_value import DirectoryServiceHybridUpdateValue


class DirectoryServiceHybridUpdateInfoEntry(BaseModel):
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    InitiatedBy: StrictStr | None = None
    NewValue: DirectoryServiceHybridUpdateValue | None = None
    PreviousValue: DirectoryServiceHybridUpdateValue | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    AssessmentId: StrictStr | None = None
