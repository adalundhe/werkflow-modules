from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_notify_configuration_filter import EndUserMessagingNotifyConfigurationFilter


class EndUserMessagingDescribeNotifyConfigurationsRequest(BaseModel):
    NotifyConfigurationIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingNotifyConfigurationFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
