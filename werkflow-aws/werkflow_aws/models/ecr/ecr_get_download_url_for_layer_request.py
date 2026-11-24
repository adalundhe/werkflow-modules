from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRGetDownloadUrlForLayerRequest(BaseModel):
    repositoryName: StrictStr
    layerDigest: StrictStr
    registryId: StrictStr | None = None
