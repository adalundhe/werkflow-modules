from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncGetBulkPublishDetailsRequest(BaseModel):
    IdentityPoolId: StrictStr
