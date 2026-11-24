from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCreateUserPoolReplicaRequest(BaseModel):
    UserPoolId: StrictStr
    RegionName: StrictStr
    UserPoolTags: dict[StrictStr, StrictStr] | None = None
