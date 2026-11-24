from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueForgeMultiStringField(BaseModel):
    contextId: StrictStr | None = None
    type: StrictStr | None = None
    values: list[StrictStr] | None = None
