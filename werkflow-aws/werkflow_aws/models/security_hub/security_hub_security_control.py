from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_parameter_configuration import SecurityHubParameterConfiguration


class SecurityHubSecurityControl(BaseModel):
    SecurityControlId: StrictStr | None = None
    SecurityControlArn: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    RemediationUrl: StrictStr | None = None
    SeverityRating: StrictStr | None = None
    SecurityControlStatus: StrictStr | None = None
    UpdateStatus: StrictStr | None = None
    Parameters: dict[StrictStr, SecurityHubParameterConfiguration] | None = None
    LastUpdateReason: StrictStr | None = None
    Provider: StrictStr | None = None
