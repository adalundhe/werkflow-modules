from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSClusterServiceConnectDefaultsRequest(BaseModel):
    namespace: StrictStr
