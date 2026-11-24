from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncRecord(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    SyncCount: StrictInt | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    DeviceLastModifiedDate: datetime.datetime | StrictStr | None = None
