from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CustomFieldOption(BaseModel):
    self: StrictStr | None = None
    value: StrictStr | None = None
