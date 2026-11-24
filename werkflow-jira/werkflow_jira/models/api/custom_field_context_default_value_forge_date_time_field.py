from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldContextDefaultValueForgeDateTimeField(BaseModel):
    contextId: StrictStr | None = None
    dateTime: StrictStr | None = None
    type: StrictStr | None = None
    useCurrent: StrictBool | None = None
