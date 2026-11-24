from __future__ import annotations
from pydantic import BaseModel
from .avatar import Avatar


class Avatars(BaseModel):
    custom: list[Avatar] | None = None
    system: list[Avatar] | None = None
