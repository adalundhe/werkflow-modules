from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDescribeConfigurationRecorderStatusRequest(BaseModel):
    ConfigurationRecorderNames: list[StrictStr] | None = None
    ServicePrincipal: StrictStr | None = None
    Arn: StrictStr | None = None
