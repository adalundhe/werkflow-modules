from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicInitiateLayerUploadRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
