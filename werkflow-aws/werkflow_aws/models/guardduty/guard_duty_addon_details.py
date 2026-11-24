from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAddonDetails(BaseModel):
    AddonVersion: StrictStr | None = None
    AddonStatus: StrictStr | None = None
