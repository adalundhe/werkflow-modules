from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncBulkPublishRequest(BaseModel):
    IdentityPoolId: StrictStr
