from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_environment_language import CodeBuildEnvironmentLanguage


class CodeBuildEnvironmentPlatform(BaseModel):
    platform: StrictStr | None = None
    languages: list[CodeBuildEnvironmentLanguage] | None = None
