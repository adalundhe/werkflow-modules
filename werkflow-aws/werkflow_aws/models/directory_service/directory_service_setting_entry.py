from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceSettingEntry(BaseModel):
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    AppliedValue: StrictStr | None = None
    RequestedValue: StrictStr | None = None
    RequestStatus: StrictStr | None = None
    RequestDetailedStatus: dict[StrictStr, StrictStr] | None = None
    RequestStatusMessage: StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    LastRequestedDateTime: datetime.datetime | StrictStr | None = None
    DataType: StrictStr | None = None
