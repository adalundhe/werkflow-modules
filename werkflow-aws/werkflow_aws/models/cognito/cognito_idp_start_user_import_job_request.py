from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPStartUserImportJobRequest(BaseModel):
    UserPoolId: StrictStr
    JobId: StrictStr
