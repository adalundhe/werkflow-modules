from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .user_filter import UserFilter


class CustomFieldContextSingleUserPickerDefaults(BaseModel):
    accountId: StrictStr | None = None
    contextId: StrictStr | None = None
    type: StrictStr | None = None
    userFilter: UserFilter | None = None
