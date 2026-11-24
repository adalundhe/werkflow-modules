from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPListUserPoolClientSecretsRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    NextToken: StrictStr | None = None
