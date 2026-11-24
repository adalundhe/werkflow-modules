from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2ClientRouteEnforcementOptions(BaseModel):
    Enforced: StrictBool | None = None
