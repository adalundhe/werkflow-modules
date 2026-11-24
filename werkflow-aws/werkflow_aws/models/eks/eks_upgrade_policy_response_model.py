from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSUpgradePolicyResponseModel(BaseModel):
    supportType: StrictStr | None = None
