from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_build_batch_filter import CodeBuildBuildBatchFilter


class CodeBuildListBuildBatchesForProjectRequest(BaseModel):
    projectName: StrictStr | None = None
    filter: CodeBuildBuildBatchFilter | None = None
    maxResults: StrictInt | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
