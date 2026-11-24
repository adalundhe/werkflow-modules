from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteRegistrationAttachmentResponse(BaseModel):
    RegistrationAttachmentArn: StrictStr | None = None
    RegistrationAttachmentId: StrictStr | None = None
    AttachmentStatus: StrictStr | None = None
    AttachmentUploadErrorReason: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
