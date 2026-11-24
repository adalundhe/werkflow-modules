from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraColorInput(BaseModel):
    name: StrictStr | None = None
