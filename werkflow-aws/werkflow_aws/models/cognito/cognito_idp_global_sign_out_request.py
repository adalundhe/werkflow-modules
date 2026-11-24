from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGlobalSignOutRequest(BaseModel):
    AccessToken: StrictStr
