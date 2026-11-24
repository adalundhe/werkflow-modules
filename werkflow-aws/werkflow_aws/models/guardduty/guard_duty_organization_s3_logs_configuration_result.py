from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationS3LogsConfigurationResult(BaseModel):
    AutoEnable: StrictBool | None = None
