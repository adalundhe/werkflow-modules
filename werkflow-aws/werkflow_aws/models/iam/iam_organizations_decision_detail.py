from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IAMOrganizationsDecisionDetail(BaseModel):
    AllowedByOrganizations: StrictBool | None = None
