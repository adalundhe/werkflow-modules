from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerRegisterAccountRequest(BaseModel):
    kmsKey: StrictStr | None = None
    delegatedAdminAccount: StrictStr | None = None
