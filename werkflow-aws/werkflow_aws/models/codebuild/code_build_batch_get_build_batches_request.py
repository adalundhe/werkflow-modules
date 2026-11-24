from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetBuildBatchesRequest(BaseModel):
    ids: list[StrictStr]
