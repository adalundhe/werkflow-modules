from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_version_information import EndUserMessagingRegistrationVersionInformation


class EndUserMessagingDescribeRegistrationVersionsResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    RegistrationVersions: list[EndUserMessagingRegistrationVersionInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
