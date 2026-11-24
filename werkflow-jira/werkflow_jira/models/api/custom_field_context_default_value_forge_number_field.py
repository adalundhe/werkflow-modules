from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CustomFieldContextDefaultValueForgeNumberField(BaseModel):
    contextId: StrictStr | None = None
    number: StrictFloat | StrictInt | None = None
    type: StrictStr | None = None
