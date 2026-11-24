from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetMLTransformRequest(BaseModel):
    TransformId: StrictStr
