from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPUpdateUserPoolReplicaRequest(BaseModel):
    UserPoolId: StrictStr
    RegionName: StrictStr
    Status: Literal['ACTIVE', 'INACTIVE']
