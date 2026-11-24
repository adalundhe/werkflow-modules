from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexDataPrivacy(BaseModel):
    childDirected: StrictBool | None = None
