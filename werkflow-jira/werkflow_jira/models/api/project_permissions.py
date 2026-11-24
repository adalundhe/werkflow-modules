from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ProjectPermissions(BaseModel):
    canEdit: StrictBool | None = None
