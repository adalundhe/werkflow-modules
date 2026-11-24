from __future__ import annotations
from pydantic import BaseModel, StrictBool


class OpenSearchServerlessVectorAcceleration(BaseModel):
    Enabled: StrictBool | None = None
