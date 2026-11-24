from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSControlPlanePlacementResponseModel(BaseModel):
    groupName: StrictStr | None = None
    spreadLevel: StrictStr | None = None
