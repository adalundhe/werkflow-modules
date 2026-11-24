from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateIAMPolicyAssignmentResponse(BaseModel):
    AssignmentName: StrictStr | None = None
    AssignmentId: StrictStr | None = None
    AssignmentStatus: StrictStr | None = None
    PolicyArn: StrictStr | None = None
    Identities: dict[StrictStr, list[StrictStr]] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
