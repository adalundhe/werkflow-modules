from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSelfUpgradeConfiguration(BaseModel):
    SelfUpgradeStatus: StrictStr | None = None
