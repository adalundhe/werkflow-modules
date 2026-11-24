from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminDeleteSoftwareTokenRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
