from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_attachment_details import SupportAttachmentDetails


class SupportCommunication(BaseModel):
    caseId: StrictStr | None = None
    body: StrictStr | None = None
    submittedBy: StrictStr | None = None
    timeCreated: StrictStr | None = None
    attachments: list[SupportAttachmentDetails] | None = None
    attachmentSet: list[SupportAttachmentDetails] | None = None
