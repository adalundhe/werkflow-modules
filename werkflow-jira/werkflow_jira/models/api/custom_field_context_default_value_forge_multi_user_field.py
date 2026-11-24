from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueForgeMultiUserField(BaseModel):
    accountIds: list[StrictStr] | None = None
    contextId: StrictStr | None = None
    type: StrictStr | None = None
