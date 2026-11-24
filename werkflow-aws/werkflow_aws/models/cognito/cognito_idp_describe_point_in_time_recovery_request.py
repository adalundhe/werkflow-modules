from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribePointInTimeRecoveryRequest(BaseModel):
    UserPoolId: StrictStr
    RestoreId: StrictStr
