from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateIAMPolicyAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
    AssignmentName: StrictStr
    Namespace: StrictStr
    AssignmentStatus: Literal['ENABLED', 'DRAFT', 'DISABLED'] | None = None
    PolicyArn: StrictStr | None = None
    Identities: dict[StrictStr, list[StrictStr]] | None = None
