from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_registration_attachments_information import EndUserMessagingRegistrationAttachmentsInformation


class EndUserMessagingDescribeRegistrationAttachmentsResponse(BaseModel):
    RegistrationAttachments: list[EndUserMessagingRegistrationAttachmentsInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
