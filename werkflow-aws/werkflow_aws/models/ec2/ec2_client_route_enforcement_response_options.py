from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2ClientRouteEnforcementResponseOptions(BaseModel):
    Enforced: StrictBool | None = None
