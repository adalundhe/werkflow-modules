from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_registration_attachment_filter import EndUserMessagingRegistrationAttachmentFilter


class EndUserMessagingDescribeRegistrationAttachmentsRequest(BaseModel):
    RegistrationAttachmentIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingRegistrationAttachmentFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
