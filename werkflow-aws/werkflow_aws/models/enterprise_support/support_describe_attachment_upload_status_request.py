from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeAttachmentUploadStatusRequest(BaseModel):
    uploadId: StrictStr
    dryRun: StrictBool | None = None
