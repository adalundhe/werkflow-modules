from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_type_definition import EndUserMessagingRegistrationTypeDefinition


class EndUserMessagingDescribeRegistrationTypeDefinitionsResponse(BaseModel):
    RegistrationTypeDefinitions: list[EndUserMessagingRegistrationTypeDefinition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
