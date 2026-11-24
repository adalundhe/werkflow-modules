from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRLifecyclePolicyRuleAction(BaseModel):
    type: StrictStr | None = None
    targetStorageClass: StrictStr | None = None
