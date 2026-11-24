from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPAdminSetUserPasswordRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    Password: StrictStr
    Permanent: StrictBool | None = None
