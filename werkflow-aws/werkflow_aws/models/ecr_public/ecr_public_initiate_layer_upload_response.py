from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ECRPublicInitiateLayerUploadResponse(BaseModel):
    uploadId: StrictStr | None = None
    partSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
