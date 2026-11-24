from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightIdentityCenterConfiguration(BaseModel):
    EnableIdentityPropagation: StrictBool | None = None
