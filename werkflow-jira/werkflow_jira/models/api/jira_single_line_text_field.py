from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraSingleLineTextField(BaseModel):
    fieldId: StrictStr | None = None
    text: StrictStr | None = None
