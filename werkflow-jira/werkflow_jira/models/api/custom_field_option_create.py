from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldOptionCreate(BaseModel):
    disabled: StrictBool | None = None
    optionId: StrictStr | None = None
    value: StrictStr | None = None
