from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeUserImportJobRequest(BaseModel):
    UserPoolId: StrictStr
    JobId: StrictStr
