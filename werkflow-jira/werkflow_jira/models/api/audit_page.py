from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .audit_entry import AuditEntry


class AuditPage(BaseModel):
    entries: list[AuditEntry] | None = None
    isLast: StrictBool | None = None
    nextPageToken: StrictStr | None = None
    nextPageURL: StrictStr | None = None
