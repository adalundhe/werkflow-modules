from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteUserPoolReplicaRequest(BaseModel):
    UserPoolId: StrictStr
    RegionName: StrictStr
