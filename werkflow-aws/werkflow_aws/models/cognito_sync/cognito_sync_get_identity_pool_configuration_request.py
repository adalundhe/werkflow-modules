from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncGetIdentityPoolConfigurationRequest(BaseModel):
    IdentityPoolId: StrictStr
