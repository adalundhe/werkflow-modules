from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteDomainConfigurationRequest(BaseModel):
    domainConfigurationName: StrictStr
