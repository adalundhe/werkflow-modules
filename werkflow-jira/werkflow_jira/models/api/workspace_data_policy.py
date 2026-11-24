from __future__ import annotations
from pydantic import BaseModel, StrictBool


class WorkspaceDataPolicy(BaseModel):
    anyContentBlocked: StrictBool | None = None
