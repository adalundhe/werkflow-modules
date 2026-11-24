from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightDescribeRoleCustomPermissionRequest(BaseModel):
    Role: Literal['ADMIN', 'AUTHOR', 'READER', 'ADMIN_PRO', 'AUTHOR_PRO', 'READER_PRO']
    AwsAccountId: StrictStr
    Namespace: StrictStr
