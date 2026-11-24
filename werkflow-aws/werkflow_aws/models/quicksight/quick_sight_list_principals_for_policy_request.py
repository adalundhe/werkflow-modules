from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListPrincipalsForPolicyRequest(BaseModel):
    AccountId: StrictStr
    PolicyArn: StrictStr
    PrincipalType: Literal['USER', 'GROUP', 'ACCOUNT'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
