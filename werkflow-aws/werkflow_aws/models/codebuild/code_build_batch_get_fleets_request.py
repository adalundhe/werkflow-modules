from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetFleetsRequest(BaseModel):
    names: list[StrictStr]
