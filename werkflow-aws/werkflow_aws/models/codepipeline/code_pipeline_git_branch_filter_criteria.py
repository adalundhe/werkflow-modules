from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineGitBranchFilterCriteria(BaseModel):
    includes: list[StrictStr] | None = None
    excludes: list[StrictStr] | None = None
