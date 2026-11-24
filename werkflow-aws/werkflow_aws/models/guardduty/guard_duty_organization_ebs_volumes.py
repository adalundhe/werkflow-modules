from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationEbsVolumes(BaseModel):
    AutoEnable: StrictBool | None = None
