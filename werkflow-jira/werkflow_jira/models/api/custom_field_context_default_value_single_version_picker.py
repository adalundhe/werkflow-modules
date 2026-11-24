from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueSingleVersionPicker(BaseModel):
    contextId: StrictStr | None = None
    type: StrictStr | None = None
    versionId: StrictStr | None = None
    versionOrder: StrictStr | None = None
