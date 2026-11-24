from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ManagedResourceVisibilitySettings(BaseModel):
    DefaultVisibility: StrictStr | None = None
