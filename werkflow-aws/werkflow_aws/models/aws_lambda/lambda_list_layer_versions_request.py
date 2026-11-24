from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListLayerVersionsRequest(BaseModel):
    LayerName: StrictStr
    CompatibleArchitecture: Literal['x86_64', 'arm64'] | None = None
    CompatibleRuntime: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
