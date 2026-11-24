from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserAttributesRequest(BaseModel):
    UserAttributeNames: list[StrictStr]
    AccessToken: StrictStr
