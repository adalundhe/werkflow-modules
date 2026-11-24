from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteBuildBatchRequest(BaseModel):
    id: StrictStr
