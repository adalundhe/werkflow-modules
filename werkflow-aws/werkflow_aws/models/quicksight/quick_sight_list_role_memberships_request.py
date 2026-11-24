from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListRoleMembershipsRequest(BaseModel):
    Role: Literal['ADMIN', 'AUTHOR', 'READER', 'ADMIN_PRO', 'AUTHOR_PRO', 'READER_PRO']
    AwsAccountId: StrictStr
    Namespace: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
