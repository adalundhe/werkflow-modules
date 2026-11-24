from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_configuration_set_information import EndUserMessagingConfigurationSetInformation


class EndUserMessagingDescribeConfigurationSetsResponse(BaseModel):
    ConfigurationSets: list[EndUserMessagingConfigurationSetInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
