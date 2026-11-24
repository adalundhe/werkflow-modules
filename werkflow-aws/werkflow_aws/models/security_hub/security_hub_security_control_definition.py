from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_parameter_definition import SecurityHubParameterDefinition


class SecurityHubSecurityControlDefinition(BaseModel):
    SecurityControlId: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    RemediationUrl: StrictStr | None = None
    SeverityRating: StrictStr | None = None
    CurrentRegionAvailability: StrictStr | None = None
    CustomizableProperties: list[StrictStr] | None = None
    ParameterDefinitions: dict[StrictStr, SecurityHubParameterDefinition] | None = None
    Provider: StrictStr | None = None
