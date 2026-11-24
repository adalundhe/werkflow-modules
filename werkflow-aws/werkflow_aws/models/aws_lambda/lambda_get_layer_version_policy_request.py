from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaGetLayerVersionPolicyRequest(BaseModel):
    LayerName: StrictStr
    VersionNumber: StrictInt
