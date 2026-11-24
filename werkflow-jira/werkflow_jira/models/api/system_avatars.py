from __future__ import annotations
from pydantic import BaseModel
from .avatar import Avatar


class SystemAvatars(BaseModel):
    system: list[Avatar] | None = None
