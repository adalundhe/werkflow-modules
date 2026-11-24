from __future__ import annotations
from pydantic import BaseModel
from .board_payload import BoardPayload


class BoardsPayload(BaseModel):
    boards: list[BoardPayload] | None = None
