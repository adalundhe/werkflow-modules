from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_protect_configuration_information import EndUserMessagingProtectConfigurationInformation


class EndUserMessagingDescribeProtectConfigurationsResponse(BaseModel):
    ProtectConfigurations: list[EndUserMessagingProtectConfigurationInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
