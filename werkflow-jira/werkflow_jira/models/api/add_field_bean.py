from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AddFieldBean(BaseModel):
    fieldId: StrictStr | None = None
