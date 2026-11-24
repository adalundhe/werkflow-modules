from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPStopUserImportJobRequest(BaseModel):
    UserPoolId: StrictStr
    JobId: StrictStr
