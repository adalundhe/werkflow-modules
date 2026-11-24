from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncGetCognitoEventsRequest(BaseModel):
    IdentityPoolId: StrictStr
