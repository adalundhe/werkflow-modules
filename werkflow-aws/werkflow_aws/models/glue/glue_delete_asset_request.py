from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteAssetRequest(BaseModel):
    Identifier: StrictStr
