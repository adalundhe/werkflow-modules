from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_version_filter import EndUserMessagingRegistrationVersionFilter


class EndUserMessagingDescribeRegistrationVersionsRequest(BaseModel):
    RegistrationId: StrictStr
    VersionNumbers: list[StrictInt] | None = None
    Filters: list[EndUserMessagingRegistrationVersionFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
