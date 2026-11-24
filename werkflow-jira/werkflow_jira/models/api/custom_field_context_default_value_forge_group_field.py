from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueForgeGroupField(BaseModel):
    contextId: StrictStr | None = None
    groupId: StrictStr | None = None
    type: StrictStr | None = None
