from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UserPickerUser(BaseModel):
    accountId: StrictStr | None = None
    accountType: StrictStr | None = None
    avatarUrl: StrictStr | None = None
    displayName: StrictStr | None = None
    html: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
