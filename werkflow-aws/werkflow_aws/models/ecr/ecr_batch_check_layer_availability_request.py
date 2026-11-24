from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRBatchCheckLayerAvailabilityRequest(BaseModel):
    repositoryName: StrictStr
    layerDigests: list[StrictStr]
    registryId: StrictStr | None = None
