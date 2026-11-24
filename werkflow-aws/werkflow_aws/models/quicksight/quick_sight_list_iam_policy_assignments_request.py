from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListIAMPolicyAssignmentsRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    AssignmentStatus: Literal['ENABLED', 'DRAFT', 'DISABLED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
