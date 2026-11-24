from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .support_upload_progress import SupportUploadProgress


class SupportDescribeAttachmentUploadStatusResponse(BaseModel):
    uploadStatus: StrictStr | None = None
    fileName: StrictStr | None = None
    uploadProgress: SupportUploadProgress | None = None
    ResponseMetadata: dict[str, Any] | None = None
