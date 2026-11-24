from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .support_completed_upload import SupportCompletedUpload


class SupportCompleteAttachmentUploadRequest(BaseModel):
    uploadId: StrictStr
    completedUploads: list[SupportCompletedUpload]
    dryRun: StrictBool | None = None
