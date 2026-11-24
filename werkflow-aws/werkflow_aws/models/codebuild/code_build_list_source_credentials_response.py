from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_source_credentials_info import CodeBuildSourceCredentialsInfo


class CodeBuildListSourceCredentialsResponse(BaseModel):
    sourceCredentialsInfos: list[CodeBuildSourceCredentialsInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
