from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleResourcePermissions(BaseModel):
    Principals: list[StrictStr] | None = None
    Actions: list[StrictStr] | None = None
