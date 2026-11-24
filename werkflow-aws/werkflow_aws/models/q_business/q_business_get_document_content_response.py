from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessGetDocumentContentResponse(BaseModel):
    presignedUrl: StrictStr | None = None
    mimeType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
