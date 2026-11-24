from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_parameter_configuration import SecurityHubParameterConfiguration


class SecurityHubUpdateSecurityControlRequest(BaseModel):
    SecurityControlId: StrictStr
    Parameters: dict[StrictStr, SecurityHubParameterConfiguration]
    LastUpdateReason: StrictStr | None = None
