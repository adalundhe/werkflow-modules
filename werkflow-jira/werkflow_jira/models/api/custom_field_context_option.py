from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldContextOption(BaseModel):
    disabled: StrictBool | None = None
    id: StrictStr | None = None
    optionId: StrictStr | None = None
    value: StrictStr | None = None
