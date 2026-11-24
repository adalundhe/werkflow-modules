from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRPublicCompleteLayerUploadResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    uploadId: StrictStr | None = None
    layerDigest: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
