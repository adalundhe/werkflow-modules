from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_filter import EndUserMessagingRegistrationFilter


class EndUserMessagingDescribeRegistrationsRequest(BaseModel):
    RegistrationIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingRegistrationFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
