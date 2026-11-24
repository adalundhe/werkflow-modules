from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlacierInitiateMultipartUploadResponse(BaseModel):
    location: StrictStr | None = None
    uploadId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
