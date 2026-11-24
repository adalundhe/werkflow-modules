from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieS3ClassificationScopeExclusion(BaseModel):
    bucketNames: list[StrictStr] | None = None
