from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_parameter_value import SecurityHubParameterValue


class SecurityHubParameterConfiguration(BaseModel):
    ValueType: StrictStr | None = None
    Value: SecurityHubParameterValue | None = None
