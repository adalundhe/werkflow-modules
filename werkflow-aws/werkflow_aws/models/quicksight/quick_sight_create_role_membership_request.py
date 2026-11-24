from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightCreateRoleMembershipRequest(BaseModel):
    MemberName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
    Role: Literal['ADMIN', 'AUTHOR', 'READER', 'ADMIN_PRO', 'AUTHOR_PRO', 'READER_PRO']
