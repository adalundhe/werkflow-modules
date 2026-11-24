from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_sandbox import CodeBuildSandbox


class CodeBuildBatchGetSandboxesResponse(BaseModel):
    sandboxes: list[CodeBuildSandbox] | None = None
    sandboxesNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
