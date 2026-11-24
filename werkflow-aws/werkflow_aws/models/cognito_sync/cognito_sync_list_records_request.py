from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncListRecordsRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    DatasetName: StrictStr
    LastSyncCount: StrictInt | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SyncSessionToken: StrictStr | None = None
