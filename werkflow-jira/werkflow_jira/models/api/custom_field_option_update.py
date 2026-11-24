from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CustomFieldOptionUpdate(BaseModel):
    disabled: StrictBool | None = None
    id: StrictStr | None = None
    value: StrictStr | None = None
