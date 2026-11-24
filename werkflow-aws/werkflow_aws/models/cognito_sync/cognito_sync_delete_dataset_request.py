from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncDeleteDatasetRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    DatasetName: StrictStr
