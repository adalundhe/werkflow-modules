from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPListUserPoolReplicasRequest(BaseModel):
    UserPoolId: StrictStr
    NextToken: StrictStr | None = None
