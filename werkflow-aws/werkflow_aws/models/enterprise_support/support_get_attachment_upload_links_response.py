from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .support_upload_url import SupportUploadUrl


class SupportGetAttachmentUploadLinksResponse(BaseModel):
    uploadId: StrictStr | None = None
    partSizeBytes: StrictInt | None = None
    totalParts: StrictInt | None = None
    nextIndex: StrictInt | None = None
    uploadUrls: list[SupportUploadUrl] | None = None
    ResponseMetadata: dict[str, Any] | None = None
