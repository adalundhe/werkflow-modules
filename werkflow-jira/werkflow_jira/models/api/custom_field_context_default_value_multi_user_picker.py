from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueMultiUserPicker(BaseModel):
    accountIds: list[StrictStr] | None = None
    contextId: StrictStr | None = None
    type: StrictStr | None = None
