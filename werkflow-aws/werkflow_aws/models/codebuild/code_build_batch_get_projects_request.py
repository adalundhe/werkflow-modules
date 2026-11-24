from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetProjectsRequest(BaseModel):
    names: list[StrictStr]
