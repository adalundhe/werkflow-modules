from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminDeleteUserAttributesRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    UserAttributeNames: list[StrictStr]
