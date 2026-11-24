from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraLabelsInput(BaseModel):
    name: StrictStr | None = None
