from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightIAMPolicyAssignment(BaseModel):
    AwsAccountId: StrictStr | None = None
    AssignmentId: StrictStr | None = None
    AssignmentName: StrictStr | None = None
    PolicyArn: StrictStr | None = None
    Identities: dict[StrictStr, list[StrictStr]] | None = None
    AssignmentStatus: StrictStr | None = None
