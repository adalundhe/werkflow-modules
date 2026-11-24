from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_country_launch_status_filter import EndUserMessagingCountryLaunchStatusFilter


class EndUserMessagingDescribeRcsAgentCountryLaunchStatusRequest(BaseModel):
    RcsAgentId: StrictStr
    IsoCountryCodes: list[StrictStr] | None = None
    Filters: list[EndUserMessagingCountryLaunchStatusFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
