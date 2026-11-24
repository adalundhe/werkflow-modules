from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxWindowsAuditLogCreateConfiguration(BaseModel):
    FileAccessAuditLogLevel: Literal['DISABLED', 'SUCCESS_ONLY', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE']
    FileShareAccessAuditLogLevel: Literal['DISABLED', 'SUCCESS_ONLY', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE']
    AuditLogDestination: StrictStr | None = None
