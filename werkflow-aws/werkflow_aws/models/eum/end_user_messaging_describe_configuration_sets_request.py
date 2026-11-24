from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_configuration_set_filter import EndUserMessagingConfigurationSetFilter


class EndUserMessagingDescribeConfigurationSetsRequest(BaseModel):
    ConfigurationSetNames: list[StrictStr] | None = None
    Filters: list[EndUserMessagingConfigurationSetFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
