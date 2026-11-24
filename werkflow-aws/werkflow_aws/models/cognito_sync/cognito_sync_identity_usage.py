from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncIdentityUsage(BaseModel):
    IdentityId: StrictStr | None = None
    IdentityPoolId: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    DatasetCount: StrictInt | None = None
    DataStorage: StrictInt | None = None
