from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_protect_configuration_filter import EndUserMessagingProtectConfigurationFilter


class EndUserMessagingDescribeProtectConfigurationsRequest(BaseModel):
    ProtectConfigurationIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingProtectConfigurationFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
