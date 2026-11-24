from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CodeBuildGitSubmodulesConfig(BaseModel):
    fetchSubmodules: StrictBool | None = None
