from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .support_upload_range import SupportUploadRange


class SupportGetAttachmentUploadLinksRequest(BaseModel):
    fileName: StrictStr
    fileSizeBytes: StrictInt | None = None
    uploadId: StrictStr | None = None
    uploadRange: SupportUploadRange | None = None
    dryRun: StrictBool | None = None
