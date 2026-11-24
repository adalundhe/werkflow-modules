from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .audit_user_avatar_urls import AuditUserAvatarUrls


class AuditUser(BaseModel):
    accountId: StrictStr | None = None
    active: StrictBool | None = None
    avatarUrls: AuditUserAvatarUrls | None = None
    displayName: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
