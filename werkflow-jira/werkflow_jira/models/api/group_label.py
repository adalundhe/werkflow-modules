from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GroupLabel(BaseModel):
    text: StrictStr | None = None
    title: StrictStr | None = None
    type: StrictStr | None = None
