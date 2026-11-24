from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightBatchPutPolicyAssignmentSuccess(BaseModel):
    PrincipalArn: StrictStr | None = None
    ReplacedPolicyArn: StrictStr | None = None
    Revision: StrictInt | None = None
