from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTUpdateDomainConfigurationResponse(BaseModel):
    domainConfigurationName: StrictStr | None = None
    domainConfigurationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
