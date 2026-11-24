from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_notify_configuration_information import EndUserMessagingNotifyConfigurationInformation


class EndUserMessagingDescribeNotifyConfigurationsResponse(BaseModel):
    NotifyConfigurations: list[EndUserMessagingNotifyConfigurationInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
