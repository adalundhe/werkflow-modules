from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSpaceQuickSightResourceDetails(BaseModel):
    resourceArn: StrictStr | None = None
