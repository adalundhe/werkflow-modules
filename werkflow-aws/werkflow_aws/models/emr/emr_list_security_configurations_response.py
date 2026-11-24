from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_security_configuration_summary import EMRSecurityConfigurationSummary


class EMRListSecurityConfigurationsResponse(BaseModel):
    SecurityConfigurations: list[EMRSecurityConfigurationSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
