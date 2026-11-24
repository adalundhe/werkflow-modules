from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_field_definition import EndUserMessagingRegistrationFieldDefinition


class EndUserMessagingDescribeRegistrationFieldDefinitionsResponse(BaseModel):
    RegistrationType: StrictStr | None = None
    RegistrationFieldDefinitions: list[EndUserMessagingRegistrationFieldDefinition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
