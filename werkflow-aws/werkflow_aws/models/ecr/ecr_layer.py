from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRLayer(BaseModel):
    layerDigest: StrictStr | None = None
    layerAvailability: StrictStr | None = None
    layerSize: StrictInt | None = None
    mediaType: StrictStr | None = None
