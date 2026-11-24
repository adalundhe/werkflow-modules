from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminConfirmSignUpRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    ClientMetadata: dict[StrictStr, StrictStr] | None = None
