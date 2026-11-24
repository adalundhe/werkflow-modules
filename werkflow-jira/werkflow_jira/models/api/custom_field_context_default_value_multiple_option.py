from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueMultipleOption(BaseModel):
    contextId: StrictStr | None = None
    optionIds: list[StrictStr] | None = None
    type: StrictStr | None = None
