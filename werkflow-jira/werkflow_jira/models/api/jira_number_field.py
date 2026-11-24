from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class JiraNumberField(BaseModel):
    fieldId: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
