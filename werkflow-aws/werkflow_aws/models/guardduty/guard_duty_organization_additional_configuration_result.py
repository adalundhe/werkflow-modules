from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyOrganizationAdditionalConfigurationResult(BaseModel):
    Name: StrictStr | None = None
    AutoEnable: StrictStr | None = None
