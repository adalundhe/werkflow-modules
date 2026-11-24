from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlacierCompleteMultipartUploadResponse(BaseModel):
    location: StrictStr | None = None
    checksum: StrictStr | None = None
    archiveId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
