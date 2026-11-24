from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRCompleteLayerUploadRequest(BaseModel):
    repositoryName: StrictStr
    uploadId: StrictStr
    layerDigests: list[StrictStr]
    registryId: StrictStr | None = None
