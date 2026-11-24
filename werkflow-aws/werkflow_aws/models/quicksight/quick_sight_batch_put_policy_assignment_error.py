from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchPutPolicyAssignmentError(BaseModel):
    PrincipalArn: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
