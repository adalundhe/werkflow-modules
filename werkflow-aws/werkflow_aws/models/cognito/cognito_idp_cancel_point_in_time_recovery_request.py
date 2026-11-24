from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCancelPointInTimeRecoveryRequest(BaseModel):
    UserPoolId: StrictStr
    RestoreId: StrictStr
