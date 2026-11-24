from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetUserPoolSessionConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
