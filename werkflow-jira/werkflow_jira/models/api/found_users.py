from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .user_picker_user import UserPickerUser


class FoundUsers(BaseModel):
    header: StrictStr | None = None
    total: StrictInt | None = None
    users: list[UserPickerUser] | None = None
