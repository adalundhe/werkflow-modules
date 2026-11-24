from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSnapmirrorSource(BaseModel):
    Path: StrictStr | None = None
