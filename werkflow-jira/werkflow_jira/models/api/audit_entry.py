from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_user import AuditUser


class AuditEntry(BaseModel):
    caller: StrictStr | None = None
    createdAt: StrictStr | None = None
    filterId: StrictStr | None = None
    jql: StrictStr | None = None
    requestUrl: StrictStr | None = None
    user: AuditUser | None = None
    userAgent: StrictStr | None = None
    validationMessage: StrictStr | None = None
