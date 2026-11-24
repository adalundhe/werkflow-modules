from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetUserPoolClientSessionConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
