from __future__ import annotations
from pydantic import BaseModel, StrictBool


class OpenSearchS3VectorsEngine(BaseModel):
    Enabled: StrictBool | None = None
