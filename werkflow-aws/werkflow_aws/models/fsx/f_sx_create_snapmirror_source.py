from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxCreateSnapmirrorSource(BaseModel):
    Path: StrictStr
