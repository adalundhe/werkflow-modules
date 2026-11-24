from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .support_attachment import SupportAttachment


class SupportAddAttachmentsToSetRequest(BaseModel):
    attachments: list[SupportAttachment]
    attachmentSetId: StrictStr | None = None
    dryRun: StrictBool | None = None
