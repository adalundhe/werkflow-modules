from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ECRGetDownloadUrlForLayerResponse(BaseModel):
    downloadUrl: StrictStr | None = None
    layerDigest: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
