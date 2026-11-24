from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldContextDefaultValueLongText(BaseModel):
    contextId: StrictStr | None = None
    text: StrictStr | None = None
    type: StrictStr | None = None
