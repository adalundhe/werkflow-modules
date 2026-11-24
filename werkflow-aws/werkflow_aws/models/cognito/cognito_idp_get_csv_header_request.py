from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetCSVHeaderRequest(BaseModel):
    UserPoolId: StrictStr
