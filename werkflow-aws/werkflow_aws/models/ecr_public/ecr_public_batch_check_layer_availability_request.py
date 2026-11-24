from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicBatchCheckLayerAvailabilityRequest(BaseModel):
    repositoryName: StrictStr
    layerDigests: list[StrictStr]
    registryId: StrictStr | None = None
