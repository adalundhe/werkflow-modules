from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieS3ClassificationScopeExclusionUpdate(BaseModel):
    bucketNames: list[StrictStr]
    operation: Literal['ADD', 'REPLACE', 'REMOVE']
