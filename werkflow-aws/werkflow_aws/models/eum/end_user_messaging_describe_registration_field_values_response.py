from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_field_value_information import EndUserMessagingRegistrationFieldValueInformation


class EndUserMessagingDescribeRegistrationFieldValuesResponse(BaseModel):
    RegistrationArn: StrictStr | None = None
    RegistrationId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    RegistrationFieldValues: list[EndUserMessagingRegistrationFieldValueInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
