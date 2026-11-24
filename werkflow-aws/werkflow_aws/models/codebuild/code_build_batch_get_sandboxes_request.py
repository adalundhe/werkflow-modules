from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetSandboxesRequest(BaseModel):
    ids: list[StrictStr]
