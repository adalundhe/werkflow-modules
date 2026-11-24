from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightAccessControlConfiguration(BaseModel):
    isACLEnabled: StrictBool | None = None
