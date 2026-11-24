from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MQLogs(BaseModel):
    Audit: StrictBool | None = None
    General: StrictBool | None = None
