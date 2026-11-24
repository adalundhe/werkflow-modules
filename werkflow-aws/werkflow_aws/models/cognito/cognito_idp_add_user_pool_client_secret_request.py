from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAddUserPoolClientSecretRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    ClientSecret: StrictStr | None = None
