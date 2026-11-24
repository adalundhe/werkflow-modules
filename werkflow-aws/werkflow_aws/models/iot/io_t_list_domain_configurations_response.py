from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_domain_configuration_summary import IoTDomainConfigurationSummary


class IoTListDomainConfigurationsResponse(BaseModel):
    domainConfigurations: list[IoTDomainConfigurationSummary] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
