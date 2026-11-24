from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_access_control_configuration_summary import KendraAccessControlConfigurationSummary


class KendraListAccessControlConfigurationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    AccessControlConfigurations: list[KendraAccessControlConfigurationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
