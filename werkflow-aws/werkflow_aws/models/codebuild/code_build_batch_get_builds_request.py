from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetBuildsRequest(BaseModel):
    ids: list[StrictStr]
