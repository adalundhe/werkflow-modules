from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeAttachmentRequest(BaseModel):
    attachmentId: StrictStr
    dryRun: StrictBool | None = None
