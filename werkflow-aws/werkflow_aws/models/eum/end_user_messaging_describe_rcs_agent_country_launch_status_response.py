from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_country_launch_status_information import EndUserMessagingCountryLaunchStatusInformation


class EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse(BaseModel):
    RcsAgentId: StrictStr | None = None
    RcsAgentArn: StrictStr | None = None
    CountryLaunchStatus: list[EndUserMessagingCountryLaunchStatusInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
