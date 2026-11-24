from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_type_filter import EndUserMessagingRegistrationTypeFilter


class EndUserMessagingDescribeRegistrationTypeDefinitionsRequest(BaseModel):
    RegistrationTypes: list[StrictStr] | None = None
    Filters: list[EndUserMessagingRegistrationTypeFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
