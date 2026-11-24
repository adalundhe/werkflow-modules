from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAddonCompatibilityDetail(BaseModel):
    name: StrictStr | None = None
    compatibleVersions: list[StrictStr] | None = None
