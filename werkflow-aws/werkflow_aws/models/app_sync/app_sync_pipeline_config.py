from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncPipelineConfig(BaseModel):
    functions: list[StrictStr] | None = None
