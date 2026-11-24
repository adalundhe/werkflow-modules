from __future__ import annotations
from pydantic import BaseModel
from .status_create import StatusCreate
from .status_scope import StatusScope


class StatusCreateRequest(BaseModel):
    scope: StatusScope | None = None
    statuses: list[StatusCreate] | None = None
