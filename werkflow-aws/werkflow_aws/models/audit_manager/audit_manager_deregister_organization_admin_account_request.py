from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDeregisterOrganizationAdminAccountRequest(BaseModel):
    adminAccountId: StrictStr | None = None
