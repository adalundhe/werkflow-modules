from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ProjectDataPolicy(BaseModel):
    anyContentBlocked: StrictBool | None = None
