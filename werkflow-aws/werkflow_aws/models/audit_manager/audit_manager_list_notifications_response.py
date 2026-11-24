from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_notification import AuditManagerNotification


class AuditManagerListNotificationsResponse(BaseModel):
    notifications: list[AuditManagerNotification] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
