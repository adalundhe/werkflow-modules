from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationEbsVolumesResult(BaseModel):
    AutoEnable: StrictBool | None = None
