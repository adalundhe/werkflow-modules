from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteMLTransformRequest(BaseModel):
    TransformId: StrictStr
