from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerCreateDelegationRequest(BaseModel):
    comment: StrictStr | None = None
    controlSetId: StrictStr | None = None
    roleArn: StrictStr | None = None
    roleType: StrictStr | None = None
