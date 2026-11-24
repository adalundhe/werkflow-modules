from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminGetUserAuthFactorsRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
