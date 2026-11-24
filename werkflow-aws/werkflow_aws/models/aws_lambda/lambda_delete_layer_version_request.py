from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaDeleteLayerVersionRequest(BaseModel):
    LayerName: StrictStr
    VersionNumber: StrictInt
