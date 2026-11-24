from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxWindowsAuditLogConfiguration(BaseModel):
    FileAccessAuditLogLevel: StrictStr | None = None
    FileShareAccessAuditLogLevel: StrictStr | None = None
    AuditLogDestination: StrictStr | None = None
