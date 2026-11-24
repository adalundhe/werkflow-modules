from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AppStreamImagePermissions(BaseModel):
    allowFleet: StrictBool | None = None
    allowImageBuilder: StrictBool | None = None
