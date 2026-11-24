from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_section_definition import EndUserMessagingRegistrationSectionDefinition


class EndUserMessagingDescribeRegistrationSectionDefinitionsResponse(BaseModel):
    RegistrationType: StrictStr | None = None
    RegistrationSectionDefinitions: list[EndUserMessagingRegistrationSectionDefinition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
