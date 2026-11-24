from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_environment_platform import CodeBuildEnvironmentPlatform


class CodeBuildListCuratedEnvironmentImagesResponse(BaseModel):
    platforms: list[CodeBuildEnvironmentPlatform] | None = None
    ResponseMetadata: dict[str, Any] | None = None
