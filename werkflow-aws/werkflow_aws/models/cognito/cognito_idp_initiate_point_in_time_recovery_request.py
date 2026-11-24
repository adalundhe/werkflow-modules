from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPInitiatePointInTimeRecoveryRequest(BaseModel):
    UserPoolId: StrictStr
    RestoreTimestamp: datetime.datetime | StrictStr
