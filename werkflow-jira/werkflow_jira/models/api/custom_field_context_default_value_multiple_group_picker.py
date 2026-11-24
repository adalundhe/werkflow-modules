from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueMultipleGroupPicker(BaseModel):
    contextId: StrictStr | None = None
    groupIds: list[StrictStr] | None = None
    type: StrictStr | None = None
