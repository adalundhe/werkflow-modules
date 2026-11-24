from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ECRUploadLayerPartResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    uploadId: StrictStr | None = None
    lastByteReceived: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
