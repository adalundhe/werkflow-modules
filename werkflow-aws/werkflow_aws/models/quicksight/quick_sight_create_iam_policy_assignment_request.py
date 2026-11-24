from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightCreateIAMPolicyAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
    AssignmentName: StrictStr
    AssignmentStatus: Literal['ENABLED', 'DRAFT', 'DISABLED']
    Namespace: StrictStr
    PolicyArn: StrictStr | None = None
    Identities: dict[StrictStr, list[StrictStr]] | None = None
