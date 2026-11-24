from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPutAssignmentEntry(BaseModel):
    PrincipalArn: StrictStr
    ExistingPolicyArn: StrictStr | None = None
    Revision: StrictInt | None = None
