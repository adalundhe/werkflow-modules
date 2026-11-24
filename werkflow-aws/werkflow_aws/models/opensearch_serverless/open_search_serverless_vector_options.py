from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessVectorOptions(BaseModel):
    ServerlessVectorAcceleration: StrictStr | None = None
