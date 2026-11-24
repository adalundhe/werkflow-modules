from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldContextDefaultValueDate(BaseModel):
    contextId: StrictStr | None = None
    date: StrictStr | None = None
    type: StrictStr | None = None
    useCurrent: StrictBool | None = None
