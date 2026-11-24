from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueForgeStringField(BaseModel):
    contextId: StrictStr | None = None
    text: StrictStr | None = None
    type: StrictStr | None = None
