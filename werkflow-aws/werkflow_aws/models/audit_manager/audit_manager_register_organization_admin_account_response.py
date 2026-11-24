from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AuditManagerRegisterOrganizationAdminAccountResponse(BaseModel):
    adminAccountId: StrictStr | None = None
    organizationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
