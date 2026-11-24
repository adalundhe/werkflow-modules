from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueSingleOption(BaseModel):
    contextId: StrictStr | None = None
    optionId: StrictStr | None = None
    type: StrictStr | None = None
