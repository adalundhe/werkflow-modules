from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPStartPointInTimeRecoveryRequest(BaseModel):
    UserPoolId: StrictStr
    RestoreId: StrictStr
