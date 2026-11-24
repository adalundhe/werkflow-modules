from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncIdentityPoolUsage(BaseModel):
    IdentityPoolId: StrictStr | None = None
    SyncSessionsCount: StrictInt | None = None
    DataStorage: StrictInt | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
