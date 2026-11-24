from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationAttachmentsInformation(BaseModel):
    RegistrationAttachmentArn: StrictStr | None = None
    RegistrationAttachmentId: StrictStr | None = None
    AttachmentStatus: StrictStr | None = None
    AttachmentUploadErrorReason: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    AttachmentUrl: StrictStr | None = None
