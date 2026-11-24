from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncSetCognitoEventsRequest(BaseModel):
    IdentityPoolId: StrictStr
    Events: dict[StrictStr, StrictStr]
