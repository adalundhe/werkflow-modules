from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDomainConfigurationSummary(BaseModel):
    domainConfigurationName: StrictStr | None = None
    domainConfigurationArn: StrictStr | None = None
    serviceType: StrictStr | None = None
