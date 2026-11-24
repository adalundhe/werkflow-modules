from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlacierUploadMultipartPartResponse(BaseModel):
    checksum: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
