from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetAssetRequest(BaseModel):
    Identifier: StrictStr
