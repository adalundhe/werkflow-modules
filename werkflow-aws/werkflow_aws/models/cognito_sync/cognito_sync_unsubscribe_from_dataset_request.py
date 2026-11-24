from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncUnsubscribeFromDatasetRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    DatasetName: StrictStr
    DeviceId: StrictStr
