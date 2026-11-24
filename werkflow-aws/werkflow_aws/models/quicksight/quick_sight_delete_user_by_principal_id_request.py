from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteUserByPrincipalIdRequest(BaseModel):
    PrincipalId: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
