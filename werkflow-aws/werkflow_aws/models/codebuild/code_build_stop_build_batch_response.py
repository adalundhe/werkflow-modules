from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_build_batch import CodeBuildBuildBatch


class CodeBuildStopBuildBatchResponse(BaseModel):
    buildBatch: CodeBuildBuildBatch | None = None
    ResponseMetadata: dict[str, Any] | None = None
