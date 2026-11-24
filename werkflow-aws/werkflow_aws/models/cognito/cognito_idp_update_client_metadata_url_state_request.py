from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPUpdateClientMetadataURLStateRequest(BaseModel):
    UserPoolId: StrictStr
    CIMDPolicyId: StrictStr
    URL: StrictStr
    Action: Literal['REFRESH', 'INVALIDATE']
