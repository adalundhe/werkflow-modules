from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ChangedValueBean(BaseModel):
    changedFrom: StrictStr | None = None
    changedTo: StrictStr | None = None
    fieldName: StrictStr | None = None
