from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_parameter_configuration import SecurityHubParameterConfiguration


class SecurityHubSecurityControlCustomParameter(BaseModel):
    SecurityControlId: StrictStr | None = None
    Parameters: dict[StrictStr, SecurityHubParameterConfiguration] | None = None
