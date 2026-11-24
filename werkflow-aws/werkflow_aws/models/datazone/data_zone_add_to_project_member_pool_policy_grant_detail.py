from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneAddToProjectMemberPoolPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
