from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraUrlField(BaseModel):
    fieldId: StrictStr | None = None
    url: StrictStr | None = None
