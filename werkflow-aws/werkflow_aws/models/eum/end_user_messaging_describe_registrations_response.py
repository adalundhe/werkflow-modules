from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_information import EndUserMessagingRegistrationInformation


class EndUserMessagingDescribeRegistrationsResponse(BaseModel):
    Registrations: list[EndUserMessagingRegistrationInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
