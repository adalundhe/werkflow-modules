from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueMultipleVersionPicker(BaseModel):
    contextId: StrictStr | None = None
    type: StrictStr | None = None
    versionIds: list[StrictStr] | None = None
    versionOrder: StrictStr | None = None
