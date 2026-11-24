from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_build_batch import CodeBuildBuildBatch


class CodeBuildBatchGetBuildBatchesResponse(BaseModel):
    buildBatches: list[CodeBuildBuildBatch] | None = None
    buildBatchesNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
