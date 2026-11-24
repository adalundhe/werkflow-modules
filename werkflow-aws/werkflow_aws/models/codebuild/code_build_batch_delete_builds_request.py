from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchDeleteBuildsRequest(BaseModel):
    ids: list[StrictStr]
