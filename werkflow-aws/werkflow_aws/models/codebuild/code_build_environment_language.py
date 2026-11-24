from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_environment_image import CodeBuildEnvironmentImage


class CodeBuildEnvironmentLanguage(BaseModel):
    language: StrictStr | None = None
    images: list[CodeBuildEnvironmentImage] | None = None
