from __future__ import annotations
from pydantic import BaseModel, StrictBool


class PollyFlushStreamConfiguration(BaseModel):
    Force: StrictBool | None = None
