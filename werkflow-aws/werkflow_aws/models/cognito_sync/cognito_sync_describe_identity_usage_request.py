from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncDescribeIdentityUsageRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
