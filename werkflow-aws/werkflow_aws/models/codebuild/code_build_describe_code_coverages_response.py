from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_code_coverage import CodeBuildCodeCoverage


class CodeBuildDescribeCodeCoveragesResponse(BaseModel):
    nextToken: StrictStr | None = None
    codeCoverages: list[CodeBuildCodeCoverage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
