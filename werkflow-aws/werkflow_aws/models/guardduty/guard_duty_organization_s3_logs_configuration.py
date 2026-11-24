from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationS3LogsConfiguration(BaseModel):
    AutoEnable: StrictBool
